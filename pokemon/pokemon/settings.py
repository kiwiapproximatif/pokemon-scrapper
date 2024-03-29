import os

from dotenv import load_dotenv


load_dotenv()

BOT_NAME: str = 'pokemon'

SPIDER_MODULES: list[str] = ['pokemon.spiders']
NEWSPIDER_MODULE: str = 'pokemon.spiders'

FILE_NAME: str = os.environ.get('FILE_NAME', 'pokemon')
FILE_HEADERS: str = os.environ.get('FILE_HEADERS', 'name,number,types,weaknesses,stats,stats_name\n')
DEFAULT_LANG: str = os.environ.get('DEFAULT_LANG', 'fr')
DEFAULT_URL: str = os.environ.get('DEFAULT_URL', f'https://www.pokemon.com/{DEFAULT_LANG}/pokedex')
POKEMONS_NUMBER: int = os.environ.get('POKEMON_NUMBER', 906)
BATCH_SIZE: int = os.environ.get('BATCH_SIZE', 100)

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'pokemons (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY: bool = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'pokemons.middlewares.PokemonsSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'pokemons.middlewares.PokemonsDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES: dict = {
    'pokemon.pipelines.PokemonPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
