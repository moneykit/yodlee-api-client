# UserDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preferences** | [**UserResponsePreferences**](UserResponsePreferences.md) |  | [optional] 
**address** | [**UserAddress**](UserAddress.md) |  | [optional] 
**phone_number** | **str** |  | [optional] 
**login_name** | **str** | The login name of the user used for authentication.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST user/register&lt;/li&gt;&lt;li&gt;GET user&lt;/li&gt;&lt;/ul&gt; | [optional] [readonly] 
**name** | [**Name**](Name.md) |  | [optional] 
**id** | **int** | The unique identifier of a consumer/user in Yodlee system for whom the API services would be accessed for.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST user/samlLogin&lt;/li&gt;&lt;li&gt;POST user/register&lt;/li&gt;&lt;li&gt;GET user&lt;/li&gt;&lt;/ul&gt; | [optional] [readonly] 
**role_type** | **str** |  | [optional] 
**email** | **str** | The email address of the user.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET user&lt;/li&gt;&lt;/ul&gt; | [optional] [readonly] 
**segment_name** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


