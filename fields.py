from azure.search.documents.indexes.models import (
    SearchFieldDataType,
    SimpleField,
    SearchableField
)

search_fields = [
        SimpleField(name="id", type=SearchFieldDataType.String, key=True),
        SearchableField(name="firstName", type=SearchFieldDataType.String, sortable=True, facetable=True, filterable=True),
        SearchableField(name="lastName", type=SearchFieldDataType.String, sortable=True, facetable=True, filterable=True),
        SearchableField(name="city", type=SearchFieldDataType.String, sortable=True, facetable=True, filterable=True),
        SearchableField(name="hobbies", type=SearchFieldDataType.String, sortable=True)
    ]