# CreateConsent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_access_frequency** | **str** | Data Access Frequency explains the number of times that this consent can be used.&lt;br&gt; Otherwise called as consent frequency type. | [optional] 
**otsp_adr_name** | **str** | Name of the Accredited Data Recipient/Organization | [optional] 
**preferences** | [**list[Preferences]**](Preferences.md) | Preferences describes options about the additional usage of data or purge data | 
**otsp_adr** | **str** | Unique/Accredition Id of the ADR | [optional] 
**client_adr** | **str** | Client Name of the ADR | 
**renewal** | [**Renewal**](Renewal.md) |  | [optional] 
**client_trusted_advisor** | [**list[ClientTrustedAdvisor]**](ClientTrustedAdvisor.md) | describes information of client trusted advisor | 
**provider_consent_id** | **str** | Provider consent id | [optional] 
**revoke_date** | **str** | Consent revoke date. | 
**title** | **str** | Title for the consent form. | 
**application_display_name** | **str** | Application display name. | 
**title_body** | **str** | Description for the title. | 
**consent_id** | **int** | Consent Id generated through POST Consent. | 
**third_party_adr** | [**list[ThirdPartyADR]**](ThirdPartyADR.md) | ThirdPartyADR describes details of additional parties which are accredited data recipients under organization | [optional] 
**provider_id** | **int** | Provider Id for which the consent needs to be generated. | 
**consent_status** | **str** | Status of the consent. | 
**scope** | [**list[Scope]**](Scope.md) | Scope describes about the consent permissions and their purpose. | 
**user_data_treatment** | [**UserDataTreatment**](UserDataTreatment.md) |  | [optional] 
**start_date** | **str** | Consent start date. | 
**expiration_date** | **str** | Consent expiry date. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


