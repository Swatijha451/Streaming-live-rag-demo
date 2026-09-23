import os,httpx
class OpenAICompatibleLLM:
 """Optional provider adapter. Corpus grounding remains enforced after generation."""
 def __init__(self): self.base=os.getenv('OPENAI_BASE_URL','https://api.openai.com/v1'); self.key=os.getenv('OPENAI_API_KEY',''); self.model=os.getenv('OPENAI_MODEL','gpt-4o-mini')
 async def generate(self,prompt):
  if not self.key: raise RuntimeError('OPENAI_API_KEY is required for provider mode; use LLM_PROVIDER=mock offline.')
  async with httpx.AsyncClient() as c:
   r=await c.post(self.base+'/chat/completions',headers={'Authorization':'Bearer '+self.key},json={'model':self.model,'messages':[{'role':'user','content':prompt}]}); r.raise_for_status(); return r.json()['choices'][0]['message']['content']
