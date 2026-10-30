# Crawl4AI (no AI extraction): how Zapier / Make / n8n / Activepieces handle broken workflows (auto-replay,
# autofix, error handlers, retries). Saves clean markdown per page; a person or a later session reads it.
import asyncio, json, os
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

URLS = [
    'https://help.zapier.com/hc/en-us/articles/8496241726989',            # Zap errors / troubleshooting
    'https://help.zapier.com/hc/en-us/articles/8496309697421',            # Autoreplay
    'https://help.zapier.com/hc/en-us/articles/22495436062605',           # Copilot / fix with AI (if moved, crawl continues)
    'https://zapier.com/blog/zapier-error-handling/',
    'https://help.zapier.com/hc/en-us/articles/8496241602189',            # Zap history
    'https://www.make.com/en/help/errors/overview-of-error-handling',
    'https://www.make.com/en/help/errors/automatic-retry-of-incomplete-executions',
    'https://docs.n8n.io/flow-logic/error-handling/',
    'https://www.activepieces.com/docs/flows/debugging-runs',
    'https://www.activepieces.com/docs/install/configuration/environment-variables',
]

async def main():
    os.makedirs('results/autofix', exist_ok=True)
    index = []
    async with AsyncWebCrawler(config=BrowserConfig(headless=True)) as c:
        for i, u in enumerate(URLS):
            r = await c.arun(u, config=CrawlerRunConfig(page_timeout=45000))
            text = (r.markdown or '') if r.success else ''
            name = f'results/autofix/{i:02d}.md'
            open(name, 'w', encoding='utf-8').write(f'<!-- {u} -->\n' + str(text)[:60000])
            index.append({'url': u, 'ok': bool(r.success), 'chars': len(str(text)), 'file': name})
            print(u, r.success, len(str(text)), flush=True)
    json.dump(index, open('results/autofix/index.json', 'w'), indent=1)
asyncio.run(main())
