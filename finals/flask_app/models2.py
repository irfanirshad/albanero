from typing import Optional
from pydantic import BaseModel, PositiveInt, validator, root_validator, constr, field_validator, ValidationError, Field

class Position(BaseModel):
    account_id: str = Field(alias='AccountID')
    average_price: str = Field(alias='AveragePrice')
    asset_type: str = Field(alias='AssetType')
    last: str = Field(alias='Last')
    bid: str = Field(alias='Bid')
    ask: str = Field(alias='Ask')
    conversion_rate: str = Field(alias='ConversionRate')
    day_trade_requirement: str = Field(alias='DayTradeRequirement')
    initial_requirement: str = Field(alias='InitialRequirement')
    position_id: str = Field(alias='PositionID')
    long_short: str = Field(alias='LongShort')
    quantity: int = Field(alias='Quantity')
    symbol: str = Field(alias='Symbol')
    timestamp: str = Field(alias='Timestamp')
    todays_profit_loss: str = Field(alias='TodaysProfitLoss')
    total_cost: str = Field(alias='TotalCost')
    market_value: str = Field(alias='MarketValue')
    mark_to_market_price: str = Field(alias='MarkToMarketPrice')
    unrealized_profit_loss: str = Field(alias='UnrealizedProfitLoss')
    unrealized_profit_loss_percent: str = Field(alias='UnrealizedProfitLossPercent')
    unrealized_profit_loss_qty: str = Field(alias='UnrealizedProfitLossQty')

# pos2 = Position({
#     "AccountID": "10",
#     "AveragePrice": "100.00",
#     "AssetType": "Equity",
#     "Last": "105.00",
#     "Bid": "102.00",
#     "Ask": "106.00",
#     "ConversionRate": "1.00",
#     "DayTradeRequirement": "50.00",
#     "InitialRequirement": "100.00",
#     "PositionID": "123",
#     "LongShort": "Long",
#     "Quantity": 100,
#     "Symbol": "AAPL",
#     "Timestamp": "2023-08-18T12:00:00",
#     "TodaysProfitLoss": "10.00",
#     "TotalCost": "10000.00",
#     "MarketValue": "10500.00",
#     "MarkToMarketPrice": "105.50",
#     "UnrealizedProfitLoss": "5.00",
#     "UnrealizedProfitLossPercent": "0.05",
#     "UnrealizedProfitLossQty": "50.00"
# })


pos2 = Position(AccountID='10', AveragePrice='100.00', AssetType='Equity', 
                Last='105.00', Bid='102.00', Ask='106.00', ConversionRate='1.00',
                DayTradeRequirement='50.00', InitialRequirement='100.00',
                PositionID='123', LongShort='Long', Quantity=100, Symbol='AAPL',
                Timestamp='2023-08-18T12:00:00', TodaysProfitLoss='10.00',
                TotalCost='10000.00', MarketValue='10500.00', MarkToMarketPrice='105.50',
                UnrealizedProfitLoss='5.00', UnrealizedProfitLossPercent='0.05',
                UnrealizedProfitLossQty='50.00')



# pos1 = Position({
#     "account_id": "10",
#     "average_price": "100.00",
#     "asset_type": "Equity",
#     "last": "105.00",
#     "bid": "102.00",
#     "ask": "106.00",
#     "conversion_rate": "1.00",
#     "day_trade_requirement": "50.00",
#     "initial_requirement": "100.00",
#     "position_id": "123",
#     "long_short": "Long",
#     "quantity": 100,
#     "symbol": "AAPL",
#     "timestamp": "2023-08-18T12:00:00",
#     "todays_profit_loss": "10.00",
#     "total_cost": "10000.00",
#     "market_value": "10500.00",
#     "mark_to_market_price": "105.50",
#     "unrealized_profit_loss": "5.00",
#     "unrealized_profit_loss_percent": "0.05",
#     "unrealized_profit_loss_qty": "50.00"
# })

pos1 = Position(account_id='10', average_price='100.00', asset_type='Equity', 
                last='105.00', bid='102.00', ask='106.00', conversion_rate='1.00',
                day_trade_requirement='50.00', initial_requirement='100.00',
                position_id='123', long_short='Long', quantity=100, symbol='AAPL',
                timestamp='2023-08-18T12:00:00', todays_profit_loss='10.00',
                total_cost='10000.00', market_value='10500.00', mark_to_market_price='105.50',
                unrealized_profit_loss='5.00', unrealized_profit_loss_percent='0.05',
                unrealized_profit_loss_qty='50.00')


print("POS 1")
# print(pos1.model_dump())
# print(pos1.model_dump(by_alias=True))
print(pos2.model_dump_json(by_alias=True))

# print("POS 2")
# print(pos2.model_dump())
# print(pos2.model_dump(by_alias=True))

