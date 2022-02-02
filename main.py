from AzureSearch import az_search
import config
import fields

# Create the search client to perform the index work
search_client = az_search.AzSearchClient(config.AZURE_SEARCH_SERVICE_NAME, config.AZURE_SEARCH_API_KEY)

index_name = 'sample-index'

# Create the index
search_client.create_index(index_name, fields.search_fields)


# Specify and create the data source and indexer to pull data from Cosmos to Search
indexer_name = 'sample-indexer'
datasource_name = 'python-cosmos-primary-person'

search_client.create_indexer(index_name, indexer_name, datasource_name, 'cosmosdb', config.COSMOS_CONNECTION_STRING, 'person')



