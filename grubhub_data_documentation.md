# TODC - GrubHub Data Documentation

## Overview
This document provides detailed explanations of the data columns and structure for the TODC GrubHub Dashboard analysis.

## Data Files Structure

### 1. Financial Summary (financial_summary.csv)
**Purpose**: High-level financial performance metrics by store and date range

| Column | Data Type | Description |
|--------|-----------|-------------|
| start_date | datetime | Start date of the reporting period |
| end_date | datetime | End date of the reporting period |
| grubhub_store_id | int64 | Unique GrubHub store identifier |
| store_number | object | Store number/identifier |
| store_name | object | Name of the store location |
| street_address | object | Store street address |
| city | object | Store city |
| state | object | Store state |
| postal_code | object | Store postal code |
| total_orders | int64 | **Key metric**: Total number of orders |
| subtotal_sales | float64 | **Key metric**: Total sales before taxes and fees |
| self_delivery_charge | float64 | Self-delivery charges |
| merchant_fees | float64 | Merchant service fees |
| sales_tax | float64 | Sales tax collected |
| tip | float64 | **Key metric**: Total tips received |
| merchant_total | float64 | Total merchant revenue |
| commission | float64 | **Key metric**: GrubHub commission (negative value) |
| delivery_commission | float64 | Delivery commission (negative value) |
| gh_plus_commission | float64 | GH+ commission (negative value) |
| order_processing_fee | float64 | Order processing fees |
| withheld_sales_tax | float64 | Sales tax withheld |
| merchant_funded_promotion_and_loyalty | float64 | Merchant-funded promotions |
| merchant_net_total | float64 | **Key metric**: Final net amount to merchant |

### 2. Operations Summary (operations_summary.csv)
**Purpose**: Operational performance metrics including cancellations, delivery times, and ratings

| Column | Data Type | Description |
|--------|-----------|-------------|
| start_date | datetime | Start date of the reporting period |
| end_date | datetime | End date of the reporting period |
| grubhub_store_id | int64 | Unique GrubHub store identifier |
| store_number | object | Store number/identifier |
| store_name | object | Name of the store location |
| street_address | object | Store street address |
| city | object | Store city |
| state | object | Store state |
| postal_code | object | Store postal code |
| total_orders | int64 | **Key metric**: Total number of orders |
| adjusted_orders | int64 | Number of adjusted orders |
| adjusted_orders_rate | float64 | Rate of adjusted orders |
| total_canceled_orders | int64 | **Key metric**: Total cancelled orders |
| total_canceled_orders_rate | float64 | **Key metric**: Cancellation rate |
| avoidable_canceled_orders | int64 | **Key metric**: Avoidable cancellations |
| avoidable_canceled_orders_rate | float64 | Rate of avoidable cancellations |
| gross_subtotal_sales | float64 | Gross sales before adjustments |
| adjusted_subtotal_sales | float64 | Sales after adjustments |
| total_canceled_orders_subtotal_sales | float64 | Sales lost to cancellations |
| avoidable_canceled_orders_subtotal_sales | float64 | Sales lost to avoidable cancellations |
| subtotal_sales_after_adjustments_and_cancels | float64 | Final sales after all adjustments |
| new_customer_orders | int64 | **Key metric**: Orders from new customers |
| new_customer_orders_rate | float64 | **Key metric**: New customer rate |
| gh_plus_customer_orders | int64 | **Key metric**: GH+ customer orders |
| gh_plus_customer_orders_rate | float64 | **Key metric**: GH+ customer rate |
| pick_up_orders | int64 | Pickup orders |
| self_delivery_orders | int64 | Self-delivery orders |
| grubhub_delivery_orders | int64 | GrubHub delivery orders |
| avg_driver_time_at_store | time | **Key metric**: Average driver wait time at store |
| avg_avoidable_driver_wait_time | time | Average avoidable driver wait time |
| avg_delivery_route_time | time | Average delivery route time |
| avg_order_to_delivery_time | time | **Key metric**: Average order to delivery time |
| ratings_all | int64 | Total ratings received |
| ratings_5_stars | int64 | **Key metric**: 5-star ratings |
| ratings_4_stars | int64 | 4-star ratings |
| ratings_3_stars | int64 | 3-star ratings |
| ratings_2_stars | int64 | 2-star ratings |
| ratings_1_star | int64 | 1-star ratings |
| reviews | int64 | Total reviews written |

### 3. Order Details (order_details.csv)
**Purpose**: Detailed information about individual orders

| Column | Data Type | Description |
|--------|-----------|-------------|
| order_channel | object | Order channel (e.g., "Marketplace") |
| order_number | object | Unique order number |
| order_date | datetime | **Key metric**: Order date |
| order_time_local | time | Order time in local timezone |
| day_of_week | object | **Key metric**: Day of the week |
| hour_of_day | object | **Key metric**: Hour of the day |
| order_time_zone | object | Timezone |
| grubhub_store_id | int64 | Unique GrubHub store identifier |
| store_number | object | Store number/identifier |
| store_name | object | Name of the store location |
| street_address | object | Store street address |
| city | object | Store city |
| state | object | Store state |
| postal_code | object | Store postal code |
| store_type | object | Type of store (e.g., "Corporate") |
| order_type | object | Type of order (e.g., "Standard Order") |
| scheduled_or_asap_order | object | Order timing (ASAP vs Scheduled) |
| fulfillment_type | object | Fulfillment method (e.g., "Grubhub Delivery") |
| cash_order | object | Whether it's a cash order |
| customer_type | object | **Key metric**: Customer type (New, Returning, Loyal) |
| gh_plus_customer | bool | **Key metric**: Whether customer has GH+ |
| order_subtotal_before_adjustments | float64 | Subtotal before adjustments |
| order_subtotal_adjustments | float64 | Subtotal adjustments |
| order_subtotal | float64 | **Key metric**: Final order subtotal |
| order_self_delivery_charge | float64 | Self-delivery charge |
| order_merchant_fees | float64 | Merchant fees |
| order_sales_tax | float64 | Sales tax |
| order_tip | float64 | **Key metric**: Order tip |
| order_total | float64 | **Key metric**: Total order amount |
| order_commission | float64 | Order commission |
| order_delivery_commission | float64 | Delivery commission |
| order_gh_plus_commission | float64 | GH+ commission |
| order_processing_fee | float64 | Processing fee |
| order_withheld_sales_tax | float64 | Withheld sales tax |
| order_merchant_funded_promotion_and_loyalty | float64 | Merchant-funded promotions |
| order_merchant_total | float64 | **Key metric**: Merchant total |
| order_time_to_expected_ready_time_minutes | int64 | Time to expected ready |
| order_time_to_actually_ready_time_minutes | int64 | Time to actually ready |
| order_time_to_driver_arrived_time_minutes | int64 | Time to driver arrival |
| order_time_to_driver_departed_time_minutes | int64 | Time to driver departure |
| order_time_to_dropoff_start_time_minutes | int64 | Time to dropoff start |
| ghd_driver_wait_time | int64 | **Key metric**: Driver wait time |
| order_on_time | object | **Key metric**: Whether order was on time |
| overall_rating_value | float64 | **Key metric**: Order rating |
| review_text | object | Customer review text |

### 4. Transactions (transactions.csv)
**Purpose**: Detailed transaction-level financial data

| Column | Data Type | Description |
|--------|-----------|-------------|
| order_channel | object | Order channel |
| order_number | object | Order number |
| transaction_date | datetime | **Key metric**: Transaction date |
| transaction_time_local | time | Transaction time |
| order_time_zone | object | Timezone |
| grubhub_store_id | int64 | Store identifier |
| store_number | object | Store number |
| store_name | object | Store name |
| street_address | object | Store address |
| city | object | Store city |
| state | object | Store state |
| postal_code | object | Store postal code |
| transaction_type | object | **Key metric**: Transaction type (Prepaid Order, Cancellation, etc.) |
| fulfillment_type | object | Fulfillment method |
| gh_plus_customer | bool | GH+ customer status |
| subtotal | float64 | **Key metric**: Transaction subtotal |
| subtotal_sales_tax | float64 | Sales tax |
| subtotal_sales_tax_exemption | float64 | Sales tax exemption |
| self_delivery_charge | float64 | Self-delivery charge |
| self_delivery_charge_tax | float64 | Self-delivery charge tax |
| self_delivery_charge_tax_exemption | float64 | Self-delivery charge tax exemption |
| merchant_service_fee | float64 | Merchant service fee |
| merchant_service_fee_tax | float64 | Merchant service fee tax |
| merchant_service_fee_tax_exemption | float64 | Merchant service fee tax exemption |
| merchant_flexible_fee_bag_fee | float64 | Bag fee |
| merchant_flexible_fee_bag_fee_tax | float64 | Bag fee tax |
| merchant_flexible_fee_bag_fee_tax_exemption | float64 | Bag fee tax exemption |
| merchant_flexible_fee_pif_fee | float64 | PIF fee |
| merchant_flexible_fee_pif_fee_tax | float64 | PIF fee tax |
| merchant_flexible_fee_pif_fee_tax_exemption | float64 | PIF fee tax exemption |
| tip | float64 | **Key metric**: Tip amount |
| merchant_total | float64 | Merchant total |
| commission | float64 | **Key metric**: Commission (negative) |
| delivery_commission | float64 | Delivery commission (negative) |
| gh_plus_commission | float64 | GH+ commission (negative) |
| processing_fee | float64 | Processing fee |
| withheld_tax | float64 | Withheld tax |
| withheld_tax_exemption | float64 | Withheld tax exemption |
| merchant_funded_promotion | float64 | Merchant-funded promotion |
| merchant_funded_loyalty | float64 | Merchant-funded loyalty |
| merchant_net_total | float64 | **Key metric**: Final net total |
| transaction_note | object | Transaction notes |
| transaction_id | object | Unique transaction ID |

### 5. Product Mix (product_mix.csv)
**Purpose**: Menu item performance analysis

| Column | Data Type | Description |
|--------|-----------|-------------|
| menu_item_category_name | object | **Key metric**: Menu category |
| menu_item_name | object | **Key metric**: Menu item name |
| quantity_sold | int64 | **Key metric**: Quantity sold |
| item_sales | float64 | **Key metric**: Revenue from this item |
| total_orders | int64 | **Key metric**: Total orders containing this item |
| new_customer_quantity_sold | int64 | Quantity sold to new customers |
| new_customer_item_sales | float64 | Revenue from new customers |
| new_customer_orders | int64 | Orders from new customers |
| loyal_customer_quantity_sold | int64 | Quantity sold to loyal customers |
| loyal_customer_item_sales | float64 | Revenue from loyal customers |
| loyal_customer_orders | int64 | Orders from loyal customers |

### 6. Cancellations (cancellations.csv)
**Purpose**: Detailed cancellation analysis

| Column | Data Type | Description |
|--------|-----------|-------------|
| order_channel | object | Order channel |
| order_number | object | Order number |
| order_date | datetime | **Key metric**: Original order date |
| order_time_local | time | Order time |
| day_of_week | object | Day of week |
| hour_of_day | object | Hour of day |
| order_time_zone | object | Timezone |
| cancellation_date | datetime | **Key metric**: Cancellation date |
| cancellation_time_local | time | Cancellation time |
| grubhub_store_id | int64 | Store identifier |
| store_number | object | Store number |
| store_name | object | Store name |
| street_address | object | Store address |
| city | object | Store city |
| state | object | Store state |
| postal_code | object | Store postal code |
| store_type | object | Store type |
| fulfillment_type | object | Fulfillment method |
| customer_type | object | Customer type |
| gh_plus_customer | bool | GH+ customer status |
| cancellation_issue | object | **Key metric**: Cancellation issue category |
| cancellation_reason | object | **Key metric**: Specific cancellation reason |
| avoidable_cancellation | object | **Key metric**: Whether cancellation was avoidable |
| voided_order_subtotal | float64 | **Key metric**: Lost revenue from subtotal |
| voided_self_delivery_charge | float64 | Lost self-delivery charge |
| voided_merchant_fees | float64 | Lost merchant fees |
| voided_sales_tax | float64 | Lost sales tax |
| voided_tip | float64 | Lost tip |
| voided_order_total | float64 | **Key metric**: Total lost revenue |
| transaction_id | object | Transaction ID |
| transaction_note | object | Transaction notes |

### 7. Deposits (deposits.csv)
**Purpose**: Payout and deposit summary information

| Column | Data Type | Description |
|--------|-----------|-------------|
| payout_date | datetime | **Key metric**: Payout date |
| payout_type | object | Type of payout (e.g., "Month End") |
| distribution_id | object | Distribution identifier |
| short_distribution_id | object | Short distribution ID |
| deposit_id | object | Deposit identifier |
| grubhub_store_id | int64 | Store identifier |
| store_number | object | Store number |
| store_name | object | Store name |
| street_address | object | Store address |
| city | object | Store city |
| state | object | Store state |
| postal_code | object | Store postal code |
| prepaid_order_count | int64 | Number of prepaid orders |
| cash_order_count | int64 | Number of cash orders |
| cancellation_order_count | int64 | Number of cancelled orders |
| order_adjustment_count | int64 | Number of order adjustments |
| on_demand_delivery_fees_count | int64 | Number of on-demand delivery fees |
| misc_payment_count | int64 | Number of miscellaneous payments |
| subtotal_sales | float64 | **Key metric**: Subtotal sales |
| cash_order_subtotal_sales_paid_at_store | float64 | Cash sales paid at store |
| subtotal_sales_adjustments | float64 | Sales adjustments |
| subtotal_voided_from_cancellations | float64 | Sales voided from cancellations |
| subtotal_sales_payout | float64 | Sales payout amount |
| sales_tax | float64 | Sales tax |
| cash_order_sales_tax_paid_at_store | float64 | Cash sales tax paid at store |
| sales_tax_adjustments | float64 | Sales tax adjustments |
| sales_tax_voided_from_cancellations | float64 | Sales tax voided from cancellations |
| withheld_sales_tax | float64 | Withheld sales tax |
| disbursed_sales_tax | float64 | Disbursed sales tax |
| self_delivery_charge | float64 | Self-delivery charge |
| merchant_service_fee | float64 | Merchant service fee |
| merchant_flexible_fees | float64 | Merchant flexible fees |
| tip | float64 | **Key metric**: Total tips |
| commission | float64 | **Key metric**: Total commission |
| delivery_commission | float64 | Delivery commission |
| on_demand_delivery_fee | float64 | On-demand delivery fee |
| gh_plus_commission | float64 | GH+ commission |
| processing_fee | float64 | Processing fee |
| merchant_funded_promotion | float64 | Merchant-funded promotion |
| merchant_funded_loyalty | float64 | Merchant-funded loyalty |
| account_adjustments | float64 | Account adjustments |
| payout_fee | float64 | Payout fee |
| payout_amount | float64 | **Key metric**: Final payout amount |

### 8. Deposit Details (deposit_details.csv)
**Purpose**: Detailed transaction-level deposit information

| Column | Data Type | Description |
|--------|-----------|-------------|
| payout_date | datetime | Payout date |
| payout_type | object | Payout type |
| store_name | object | Store name |
| street_address | object | Store address |
| grubhub_store_id | int64 | Store identifier |
| store_number | object | Store number |
| distribution_id | object | Distribution ID |
| short_distribution_id | object | Short distribution ID |
| deposit_id | object | Deposit ID |
| order_number | object | Order number |
| transaction_date | datetime | Transaction date |
| transaction_time_local | time | Transaction time |
| transaction_type | object | Transaction type |
| fulfillment_type | object | Fulfillment method |
| gh_plus_customer | bool | GH+ customer status |
| subtotal | float64 | Transaction subtotal |
| subtotal_sales_tax | float64 | Sales tax |
| subtotal_sales_tax_exemption | float64 | Sales tax exemption |
| self_delivery_charge | float64 | Self-delivery charge |
| self_delivery_charge_tax | float64 | Self-delivery charge tax |
| self_delivery_charge_tax_exemption | float64 | Self-delivery charge tax exemption |
| merchant_service_fee | float64 | Merchant service fee |
| merchant_service_fee_tax | float64 | Merchant service fee tax |
| merchant_service_fee_tax_exemption | float64 | Merchant service fee tax exemption |
| merchant_flexible_fee_bag_fee | float64 | Bag fee |
| merchant_flexible_fee_bag_fee_tax | float64 | Bag fee tax |
| merchant_flexible_fee_bag_fee_tax_exemption | float64 | Bag fee tax exemption |
| merchant_flexible_fee_pif_fee | float64 | PIF fee |
| merchant_flexible_fee_pif_fee_tax | float64 | PIF fee tax |
| merchant_flexible_fee_pif_fee_tax_exemption | float64 | PIF fee tax exemption |
| tip | float64 | Tip amount |
| merchant_total | float64 | Merchant total |
| commission | float64 | Commission |
| delivery_commission | float64 | Delivery commission |
| gh_plus_commission | float64 | GH+ commission |
| processing_fee | float64 | Processing fee |
| withheld_tax | float64 | Withheld tax |
| withheld_tax_exemption | float64 | Withheld tax exemption |
| merchant_funded_promotion | float64 | Merchant-funded promotion |
| merchant_funded_loyalty | float64 | Merchant-funded loyalty |
| merchant_net_total | float64 | **Key metric**: Final net total |
| transaction_id | object | Transaction ID |

## Key Metrics for Dashboard Analysis

### Financial Metrics
- **Total Sales**: Sum of `subtotal_sales` from financial_summary
- **Net Revenue**: Sum of `merchant_net_total` from financial_summary
- **Commission Rate**: `abs(commission) / subtotal_sales * 100`
- **Average Order Value**: `subtotal_sales / total_orders`
- **Total Tips**: Sum of `tip` from financial_summary

### Operational Metrics
- **Cancellation Rate**: `total_canceled_orders / total_orders * 100`
- **New Customer Rate**: `new_customer_orders / total_orders * 100`
- **GH+ Customer Rate**: `gh_plus_customer_orders / total_orders * 100`
- **Avoidable Cancellation Rate**: `avoidable_canceled_orders / total_orders * 100`
- **5-Star Rating Rate**: `ratings_5_stars / ratings_all * 100`

### Product Performance Metrics
- **Top Selling Items**: Items with highest `quantity_sold`
- **Top Revenue Items**: Items with highest `item_sales`
- **Category Performance**: Group by `menu_item_category_name`

### Time-based Analysis
- **Hourly Distribution**: Group orders by `hour_of_day`
- **Daily Distribution**: Group orders by `day_of_week`
- **Peak Hours**: Hours with highest order volume

### Customer Analysis
- **Customer Type Distribution**: Group by `customer_type` (New, Returning, Loyal)
- **GH+ vs Non-GH+**: Compare performance between GH+ and regular customers
- **Customer Lifetime Value**: Average order value by customer type

## Data Relationships

### Store Matching
All datasets use `grubhub_store_id` and `store_name` to identify stores. The `store_name` field should be consistent across all files for proper aggregation.

### Date Ranges
- Most summary files use `start_date` and `end_date` for date filtering
- Transaction and order files use `transaction_date` and `order_date`
- Cancellation files use both `order_date` and `cancellation_date`

### Customer Segmentation
- **Customer Type**: New, Returning, Loyal
- **GH+ Status**: Boolean indicating premium customer status
- **Geographic**: City, State, Postal Code

## Notes for Dashboard Implementation

1. **Date Filtering**: Use appropriate date columns for each dataset
2. **Store Filtering**: Filter by `store_name` for store-specific analysis
3. **Customer Filtering**: Use `customer_type` and `gh_plus_customer` for customer segmentation
4. **Commission Calculations**: Commission values are typically negative, use `abs()` for display
5. **Time Calculations**: Time fields may need conversion from string to numeric for calculations
6. **Rating Analysis**: Handle cases where `ratings_all` is 0 to avoid division by zero
7. **Cancellation Analysis**: Focus on `avoidable_cancellation` for operational improvements
8. **Product Mix**: Use both quantity and revenue metrics for comprehensive product analysis

## Enhanced Analytics Opportunities

### Advanced Metrics
- **Customer Acquisition Cost**: Marketing spend / new customers
- **Customer Lifetime Value**: Average order value × frequency × retention rate
- **Delivery Efficiency**: Driver wait time vs delivery time ratios
- **Revenue per Store**: Net revenue / number of stores
- **Peak Performance Analysis**: Best performing hours/days by store

### Predictive Analytics
- **Demand Forecasting**: Based on historical hourly/daily patterns
- **Cancellation Prediction**: Using avoidable cancellation patterns
- **Customer Churn Analysis**: Based on customer type transitions
- **Optimal Pricing**: Based on product performance and customer segments

### Operational Insights
- **Store Performance Benchmarking**: Compare stores within same city/state
- **Delivery Route Optimization**: Based on delivery time patterns
- **Menu Optimization**: Product mix analysis for revenue maximization
- **Customer Experience**: Rating trends and review sentiment analysis
