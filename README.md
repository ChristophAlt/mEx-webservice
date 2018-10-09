# macss-webservice

## Install

- Generate a Github access token via settings > Developer settings > Generate new token **(with scope: repo)**

- Install dependencies via pip and provide your access token with the following command:  
`GITHUB_ACCESS_TOKEN=<YOUR ACCESS TOKEN> pip install --process-dependency-links -e .`

## Usage

Run the following command with the environment variables pointing to the respective files and SOLR endpoint.

```
MACSS_MEDICAL_IE_LANGUAGE='de' \
MACSS_MEDICAL_IE_NER_MODEL_PATH='../<MACSS RESOURCE PATH>/model_ner.pt' \
MACSS_MEDICAL_IE_RE_MODEL_PATH='../<MACSS RESOURCE PATH>/model_re.pt' \
MACSS_MEDICAL_IE_NEGATION_TRIGGER_PATH='../<MACSS RESOURCE PATH>/negex_trigger_german_biotxtm_2016.txt' \
MACSS_MEDICAL_IE_DISAMBIGUATOR_PATH='../<MACSS RESOURCE PATH>/dsg_disambiguator.pkl' \
MACSS_MEDICAL_IE_UMLS_SOLR_HOST=<SOLR HOST> \
MACSS_MEDICAL_IE_UMLS_SOLR_PORT=<SOLR PORT> \
MACSS_MEDICAL_IE_UMLS_SOLR_CORE=<SOLR CORE> \
python -m macss_webservice.run
```
