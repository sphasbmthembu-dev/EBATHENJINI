# EBATHENJINI - Testing & Debugging Guide

## Unit Testing

### Running Tests
```bash
# Run all tests
python run_tests.py

# Run specific test file
python -m unittest tests.test_database -v

# Run specific test class
python -m unittest tests.test_database.TestDatabaseManager -v

# Run specific test method
python -m unittest tests.test_database.TestDatabaseManager.test_add_memory -v
```

### Test Coverage
```bash
pip install coverage
coverage run -m unittest discover
coverage report
coverage html  # Generate HTML report
```

## Integration Testing

```bash
python -m unittest tests.test_integration -v
```

## Performance Testing

```bash
python tests/test_performance.py
```

## Debug Mode

### Enable Debug Logging
```python
# app/main_app.py
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler()
    ]
)
```

### Add Debug Statements
```python
import logging
logger = logging.getLogger(__name__)

logger.debug("Adding memory: %s", title)
logger.info("Memory saved successfully")
logger.warning("Memory file not found")
logger.error("Database error: %s", error_msg)
```

## Debugging Tools

### Python Debugger (pdb)
```bash
# Add breakpoint in code
import pdb; pdb.set_trace()

# Run with debugger
python -m pdb main.py
```

### Kivy Inspector
```python
from kivy.app import App
from kivy.core.window import Window

Window.show_keyboard = True

# In build() method:
self.inspector = DebugRs(listen_host='127.0.0.1', listen_port=8020)
self.inspector.start()
```

## Common Issues & Solutions

### Database Lock
**Issue**: `sqlite3.OperationalError: database is locked`

**Solution**:
```python
conn = sqlite3.connect(self.db_path, timeout=30.0)
conn.execute('PRAGMA journal_mode=WAL')
```

### Memory Leaks
**Issue**: App crashes with high memory usage

**Solution**:
```python
# Implement cleanup
def on_stop(self):
    if hasattr(self, 'db'):
        self.db.close()
    return True
```

### Image Loading Issues
**Issue**: Images fail to load

**Solution**:
```python
from kivy.uix.image import Image
from kivy.garden.asynckivy import asynchronous

@asynchronous
def load_image(source):
    return Image(source=source)
```

### Slow Search
**Issue**: Search performance degrades with many memories

**Solution**:
```python
# Add database indexing
CREATE INDEX idx_title ON memories(title);
CREATE INDEX idx_tags ON memories(tags);
```

## Logging Best Practices

```python
import logging

# Create logger
logger = logging.getLogger(__name__)

# Log levels
logger.debug("Detailed diagnostic info")      # Development
logger.info("Confirmation things work")       # Normal operation
logger.warning("Something unexpected")        # Potential issue
logger.error("Serious problem")               # Error occurred
logger.critical("Very serious problem")       # Critical failure
```

## Network Debugging

```bash
# Monitor network traffic
wireshark

# Test API endpoints
curl -v http://api.example.com/endpoint

# Python requests debugging
import logging
logging.basicConfig(level=logging.DEBUG)
httplib2.debuglevel = 1
```

## Performance Profiling

```python
import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()

# Code to profile
app.run()

profiler.disable()
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats()
```

## Memory Profiling

```bash
pip install memory_profiler
python -m memory_profiler main.py
```

```python
from memory_profiler import profile

@profile
def my_function():
    a = [1] * (10 ** 6)
    return sum(a)
```

## Crash Reporting

```python
import sys
import traceback

def exception_handler(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    
    logger.critical(
        "Uncaught exception",
        exc_info=(exc_type, exc_value, exc_traceback)
    )

sys.excepthook = exception_handler
```

## Test Examples

```python
# Test memory validation
def test_add_invalid_memory(self):
    with self.assertRaises(ValueError):
        self.db.add_memory("", "", "")

# Test concurrent access
def test_concurrent_adds(self):
    from threading import Thread
    threads = []
    for i in range(10):
        t = Thread(
            target=self.db.add_memory,
            args=(f'Memory {i}', f'Desc {i}', '2024-01-01')
        )
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    self.assertEqual(len(self.db.get_all_memories()), 10)
```

## Continuous Integration

### GitHub Actions
```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - run: pip install -r requirements.txt
      - run: python run_tests.py
```

## Monitoring

### Application Monitoring
```python
import time

class PerformanceMonitor:
    def __init__(self):
        self.metrics = {}
    
    def record_operation(self, operation_name, duration):
        if operation_name not in self.metrics:
            self.metrics[operation_name] = []
        self.metrics[operation_name].append(duration)
    
    def get_average(self, operation_name):
        if operation_name in self.metrics:
            return sum(self.metrics[operation_name]) / len(self.metrics[operation_name])
        return 0
```
