from AzureSearch import az_search
import config
import fields

# Create the search client to perform the index work
search_client = az_search.AzSearchClient(config.AZURE_SEARCH_SERVICE_NAME, config.AZURE_SEARCH_API_KEY)

index_name = config.AZURE_SEARCH_INDEX_NAME

# Specify and create the data source and indexer to pull data from Cosmos to Search
indexer_name = 'sample-indexer'

search_client.run_indexer(indexer_name)




