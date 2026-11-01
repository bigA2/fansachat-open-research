# Crawl4AI (no AI extraction): public pages for the 1 Nov research (field mapping, nodes, notifications, pricing,
# prompt injection, licences, Vertex AI Agent Builder, O*NET releases). Clean markdown per page; a later session reads it.
import asyncio, json, os
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

TOPICS = {
    'onet': ['https://www.onetcenter.org/database.html', 'https://www.onetcenter.org/db_releases.html'],
    'mapping': ['https://help.zapier.com/hc/en-us/articles/8496343026701', 'https://help.zapier.com/hc/en-us/articles/8496288690317',
                'https://help.zapier.com/hc/en-us/articles/8495961813389', 'https://docs.n8n.io/data/data-mapping/',
                'https://docs.n8n.io/data/data-mapping/data-mapping-ui/', 'https://www.activepieces.com/docs/flows/passing-data'],
    'nodes': ['https://docs.n8n.io/workflows/components/nodes/', 'https://docs.n8n.io/integrations/builtin/node-types/',
              'https://docs.n8n.io/flow-logic/', 'https://docs.n8n.io/workflows/executions/debug/'],
    'notifications': ['https://help.zapier.com/hc/en-us/articles/8496291148685', 'https://help.zapier.com/hc/en-us/articles/8496037690637',
                      'https://help.zapier.com/hc/en-us/articles/8496181445261', 'https://docs.n8n.io/flow-logic/error-handling/',
                      'https://www.make.com/en/help/scenarios/scenario-settings'],
    'pricing': ['https://zapier.com/pricing', 'https://www.make.com/en/pricing', 'https://n8n.io/pricing/',
                'https://www.activepieces.com/pricing', 'https://www.lindy.ai/pricing', 'https://relay.app/pricing'],
    'teams': ['https://help.zapier.com/hc/en-us/articles/8496270839565', 'https://help.zapier.com/hc/en-us/articles/8496307853709',
              'https://docs.n8n.io/user-management/rbac/projects/', 'https://www.make.com/en/help/general/teams'],
    'vertex': ['https://cloud.google.com/products/agent-builder', 'https://cloud.google.com/vertex-ai/generative-ai/docs/agent-builder/overview',
               'https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview', 'https://cloud.google.com/application-integration/docs/overview'],
    'injection': ['https://genai.owasp.org/llmrisk/llm01-prompt-injection/', 'https://genai.owasp.org/llmrisk/llm072025-system-prompt-leakage/',
                  'https://genai.owasp.org/llmrisk/llm062025-excessive-agency/', 'https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/',
                  'https://genai.owasp.org/llmrisk/llm052025-improper-output-handling/', 'https://simonwillison.net/series/prompt-injection/',
                  'https://learnprompting.org/docs/prompt_hacking/injection', 'https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html'],
    'licences': ['https://github.com/obra/superpowers/blob/main/LICENSE', 'https://github.com/obra/superpowers',
                 'https://github.com/multica-ai/andrej-karpathy-skills', 'https://github.com/multica-ai/andrej-karpathy-skills/blob/main/LICENSE',
                 'https://raw.githubusercontent.com/n8n-io/n8n/master/LICENSE.md'],
}

async def main():
    index = []
    async with AsyncWebCrawler(config=BrowserConfig(headless=True)) as c:
        for topic, urls in TOPICS.items():
            os.makedirs(f'results/sources/{topic}', exist_ok=True)
            for i, u in enumerate(urls):
                try:
                    r = await c.arun(u, config=CrawlerRunConfig(page_timeout=45000))
                    ok, text = r.success, str(r.markdown or '') if r.success else ''
                except Exception as e: ok, text = False, ''
                name = f'results/sources/{topic}/{i:02d}.md'
                open(name, 'w', encoding='utf-8').write(f'<!-- {u} -->\n' + text[:60000])
                index.append({'topic': topic, 'url': u, 'ok': ok, 'chars': len(text), 'file': name})
                print(topic, u, ok, len(text), flush=True)
    json.dump(index, open('results/sources/index.json', 'w'), indent=1)
asyncio.run(main())
