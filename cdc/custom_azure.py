from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'devcentstr1' # Must be replaced by your <storage_account_name>
    account_key = 'idH3wrJJ5EBBE3VZd57iLxZC9RzGCcypZRW4NZAM5uBhr7CW+LZiu+6A0qW11nvy/Dw8JpKjyd6gp4zSzrYFIg==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'devcentstr1' # Must be replaced by your storage_account_name
    account_key = 'idH3wrJJ5EBBE3VZd57iLxZC9RzGCcypZRW4NZAM5uBhr7CW+LZiu+6A0qW11nvy/Dw8JpKjyd6gp4zSzrYFIg==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None