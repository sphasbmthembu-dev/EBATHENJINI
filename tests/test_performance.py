"""Performance benchmarks for EBATHENJINI."""

import time
import tempfile
import shutil
import os
from app.database.db_manager import DatabaseManager


class PerformanceBenchmark:
    """Performance benchmarking utilities."""

    def __init__(self):
        self.results = {}
        self.test_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.test_dir, 'bench_ebathenjini.db')
        self.db = DatabaseManager(self.db_path)

    def cleanup(self):
        """Clean up test resources."""
        shutil.rmtree(self.test_dir)

    def benchmark_add_memory(self, count=100):
        """Benchmark adding memories."""
        start = time.time()
        for i in range(count):
            self.db.add_memory(
                title=f'Memory {i}',
                description=f'This is memory number {i}',
                date_memory='2024-01-01',
                tags=f'tag{i%5}'
            )
        elapsed = time.time() - start
        self.results['add_memory'] = {
            'count': count,
            'time': elapsed,
            'avg_time': elapsed / count
        }
        print(f'Added {count} memories in {elapsed:.3f}s ({elapsed/count*1000:.2f}ms per memory)')

    def benchmark_get_all_memories(self):
        """Benchmark retrieving all memories."""
        # First add some memories
        for i in range(50):
            self.db.add_memory(f'Memory {i}', f'Desc {i}', '2024-01-01')
        
        start = time.time()
        for _ in range(10):
            self.db.get_all_memories()
        elapsed = time.time() - start
        self.results['get_all_memories'] = {
            'iterations': 10,
            'time': elapsed,
            'avg_time': elapsed / 10
        }
        print(f'Retrieved all memories 10 times in {elapsed:.3f}s ({elapsed/10*1000:.2f}ms per retrieval)')

    def benchmark_search_memories(self):
        """Benchmark searching memories."""
        # Add test data
        for i in range(100):
            self.db.add_memory(f'Memory {i}', f'Desc {i}', '2024-01-01')
        
        start = time.time()
        for _ in range(20):
            self.db.search_memories('Memory')
        elapsed = time.time() - start
        self.results['search_memories'] = {
            'searches': 20,
            'time': elapsed,
            'avg_time': elapsed / 20
        }
        print(f'Searched memories 20 times in {elapsed:.3f}s ({elapsed/20*1000:.2f}ms per search)')

    def benchmark_delete_memory(self):
        """Benchmark deleting memories."""
        # Add memories
        ids = []
        for i in range(50):
            memory_id = self.db.add_memory(f'Memory {i}', f'Desc {i}', '2024-01-01')
            ids.append(memory_id)
        
        start = time.time()
        for memory_id in ids:
            self.db.delete_memory(memory_id)
        elapsed = time.time() - start
        self.results['delete_memory'] = {
            'count': len(ids),
            'time': elapsed,
            'avg_time': elapsed / len(ids)
        }
        print(f'Deleted {len(ids)} memories in {elapsed:.3f}s ({elapsed/len(ids)*1000:.2f}ms per delete)')

    def run_all_benchmarks(self):
        """Run all benchmarks."""
        print('\n=== EBATHENJINI Performance Benchmarks ===')
        self.benchmark_add_memory(100)
        self.benchmark_get_all_memories()
        self.benchmark_search_memories()
        self.benchmark_delete_memory()
        print('\n=== Benchmark Results ===')
        for test_name, results in self.results.items():
            print(f'\n{test_name}:')
            for key, value in results.items():
                print(f'  {key}: {value}')


if __name__ == '__main__':
    bench = PerformanceBenchmark()
    bench.run_all_benchmarks()
    bench.cleanup()
