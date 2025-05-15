from pydantic import BaseModel
import wikipediaapi


# Define the Pydantic Schema
class InstitutionDetails(BaseModel):
    name: str
    founder: str
    founded: str
    branches: str
    employees: str
    summary: str

# Function to Fetch and Extract Details from Wikipedia
def fetch(institution_name):
    user_agent = "InstitutionInfoFetcher/1.0 (https://example.com; contact@example.com)"
    wiki = wikipediaapi.Wikipedia('en', headers={"User-Agent": user_agent})
    page = wiki.page(institution_name)
    content = page.text
 

    # Basic parsing for demonstration purposes
    founder = next((line for line in content.split('\n') if "founder" in line.lower()), "Not available")
    founded = next((line for line in content.split('\n') if "founded" in line.lower() or "established" in line.lower()), "Not available")
    branches = next((line for line in content.split('\n') if "branch" in line.lower()), "Not available")
    employees = next((line for line in content.split('\n') if "employee" in line.lower()), "Not available")
    summary = "\n".join(content.split('\n')[:4])

    return InstitutionDetails(
        name=institution_name,
        founder=founder,
        founded=founded,
        branches=branches,
        employees=employees,
        summary=summary
    )

details = fetch("JNNCE")
print("\nExtracted Institution Details:")
print(details.model_dump_json(indent=4))  # Use model_dump_json instead of .json()
