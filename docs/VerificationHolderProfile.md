# VerificationHolderProfile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | The primary key of the account resource and the unique identifier for the account | [optional] [readonly] 
**address** | [**list[AbstractAddress]**](AbstractAddress.md) | The account holder&#39;s address available at the profile and account levels | [optional] [readonly] 
**phone_number** | [**list[PhoneNumber]**](PhoneNumber.md) | The account holder&#39;s phone number available at the profile and account levels | [optional] [readonly] 
**provider_account_id** | **int** | The primary key of the provider account resource | [optional] [readonly] 
**holder** | [**list[VerificationHolder]**](VerificationHolder.md) | The holder entity is account-specific and captures the ownership status and the name details of the user | [optional] [readonly] 
**email** | [**list[Email]**](Email.md) | The account holder&#39;s email ID available at the profile and account levels | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


