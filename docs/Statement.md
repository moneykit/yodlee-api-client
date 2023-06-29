# Statement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apr** | **float** | The APR applied to the balance on the credit card account, as available in the statement.&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; In case of variable APR, the APR available on the statement might differ from the APR available at the account-level.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, loan, insurance&lt;br&gt; | [optional] [readonly] 
**cash_apr** | **float** | The APR applicable to cash withdrawals on the credit card account.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, loan, insurance&lt;br&gt; | [optional] [readonly] 
**billing_period_start** | **str** | The start date of the statement period.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, loan, insurance&lt;br&gt; | [optional] [readonly] 
**due_date** | **str** | The date by when the minimum payment is due to be paid.&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; The due date that appears in the statement may differ from the due date at the account-level.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, loan, insurance&lt;br&gt; | [optional] [readonly] 
**interest_amount** | [**Money**](Money.md) |  | [optional] 
**statement_date** | **str** | The date on which the statement is generated.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, loan, insurance&lt;br&gt; | [optional] [readonly] 
**cash_advance** | [**Money**](Money.md) |  | [optional] 
**billing_period_end** | **str** | The end date of the statement period.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, loan, insurance&lt;br&gt; | [optional] [readonly] 
**principal_amount** | [**Money**](Money.md) |  | [optional] 
**loan_balance** | [**Money**](Money.md) |  | [optional] 
**amount_due** | [**Money**](Money.md) |  | [optional] 
**account_id** | **int** | Account to which the statement belongs to.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, loan, insurance&lt;br&gt; | [optional] [readonly] 
**last_updated** | **str** | The date when the account was last updated by Yodlee.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, loan, insurance&lt;br&gt; | [optional] [readonly] 
**is_latest** | **bool** | The field is set to true if the statement is the latest generated statement.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, loan, insurance&lt;br&gt; | [optional] [readonly] 
**minimum_payment** | [**Money**](Money.md) |  | [optional] 
**last_payment_date** | **str** | The date on which the last payment was done during the billing cycle.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, loan, insurance&lt;br&gt; | [optional] [readonly] 
**last_payment_amount** | [**Money**](Money.md) |  | [optional] 
**id** | **int** | Unique identifier for the statement.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, loan, insurance&lt;br&gt; | [optional] [readonly] 
**new_charges** | [**Money**](Money.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


