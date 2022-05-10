"""
Tests for simple fetcher
"""

from unittest import IsolatedAsyncioTestCase
import asyncio
from fetcher import main


class TestFetcher(IsolatedAsyncioTestCase):
    """
    Tests for simple fetcher
    """
    def check(self, result):
        """
        Checks result correctness
        """
        self.assertEqual(11, len(result))
        self.assertEqual("GitHub.com", result["https://github.com/TrandeLik/map_generalization"])
        self.assertEqual("GitHub.com", result["https://github.com/TrandeLik/numerical_methods"])
        self.assertEqual("nginx", result["https://sphere.vk.company/"])
        self.assertEqual("nginx", result["https://www.mos.ru/"])
        self.assertEqual(None, result["https://yandex.ru/"])
        self.assertEqual("ESF", result["https://www.youtube.com/"])
        self.assertEqual(None, result["https://translate.yandex.ru/"])
        self.assertEqual(None, result["https://yandex.ru/pogoda/"])
        self.assertEqual(None, result["https://yandex.ru/news/quotes/1/index.html"])
        self.assertEqual(None, result["https://yandex.ru/covid19/stat"])
        self.assertEqual("kittenx", result["https://vk.com"])

    def setUp(self):
        """
        Creates event loop and opens the file before each test
        """
        self.event_loop = asyncio.get_event_loop()
        self.file = open("urls.txt", "r")

    async def test_one_worker(self):
        """
        Test with only one worker
        """
        result = await main(self.event_loop, 1, self.file)
        self.check(result)

    async def test_less_workers_than_urls(self):
        """
        Test with several workers
        """
        result = await main(self.event_loop, 3, self.file)
        self.check(result)

    async def test_worker_for_each_url(self):
        """
        Test with one worker for each url in file
        """
        result = await main(self.event_loop, 11, self.file)
        self.check(result)

    async def test_more_workers_than_urls(self):
        """
        Test with more workers than urls count
        """
        result = await main(self.event_loop, 15, self.file)
        self.check(result)
