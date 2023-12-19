import typesense_utils as tyutl
from utils import save_json

results = tyutl.search("pages_elements",{
  'q': 'Home Automation',
  'query_by': 'element_value'
})

save_json("results.json",results)
