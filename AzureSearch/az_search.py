import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient, SearchIndexerClient
from azure.search.documents import SearchClient
from azure.search.documents.indexes.models import (
    SearchIndexerDataContainer,
    SearchIndexerDataSourceConnection,
    SearchIndexer,
    ComplexField,
    CorsOptions,
    SearchIndex,
    ScoringProfile,
    SearchFieldDataType,
    SimpleField,
    SearchableField
)

class AzSearchClient:
    def __init__(self, service_name, api_key):
        self.service_name = service_name
        self.api_key = api_key
        self.endpoint = "https://{}.search.windows.net/".format(self.service_name)
    
    def create_index(self, index_name, fields):
        # Create the client with credentials
        admin_client = SearchIndexClient(endpoint=self.endpoint,
                       index_name=index_name,
                       credential=AzureKeyCredential(self.api_key))

        # Specify search index attributes
        index = SearchIndex(
            name=index_name,
            fields=fields
            )

        # Attempt to create the index
        try:
            result = admin_client.create_index(index)
            print('Index', result.name, 'created')
        except Exception as ex:
            print(ex)

    def create_indexer(self, index_name, indexer_name, datasource_name, datasource_type, connection_string, container_name):
        # Create the indexer client with credentials
        indexers_client = SearchIndexerClient(self.endpoint, AzureKeyCredential(self.api_key))

        # Create the data source
        container = SearchIndexerDataContainer(name=container_name)
        data_source_connection = SearchIndexerDataSourceConnection(
            name=datasource_name,
            type=datasource_type,
            connection_string=connection_string,
            container=container,
            data_change_detection_policy={ "@odata.type" : "#Microsoft.Azure.Search.HighWaterMarkChangeDetectionPolicy", "highWaterMarkColumnName" : "_ts" }
        )
        try:
            data_source = indexers_client.create_data_source_connection(data_source_connection)
        except Exception as ex:
            print(ex)

        # Create the indexer
        indexer = SearchIndexer(
            name=indexer_name,
            data_source_name=datasource_name,
            target_index_name=index_name
        )
        
        result = indexers_client.create_indexer(indexer)
        print("Create new Indexer - sample-indexer")
