create procedure SelectAuctionByUUID
@UUID nvarchar(255)
as 
select * from Auction where UUID = @UUID
go

create procedure SelectBidByAmountAuctionID
@BidAmount int,
@AuctionID nvarchar(255)
as 
select * from Bid inner join BidToAuction on Bid.ID = BidToAuction.BidID where BidAmount= @BidAmount and AuctionID = @AuctionID
go

create procedure SelectAuctions
as
select * from Auction
go

create procedure SelectActiveAuctions
as
select * from Auction where getdate() < EndDate;
go

create procedure SelectWeekdayAverageBIN
@ItemName as nvarchar(255)
as
select 
(select avg(cast(HighestBidAmount as bigint)) from auction where ItemName like @ItemName and claimed = 1 and bin = 1 and datename(WEEKDAY, EndDate) = 'Monday') 
as Monday,
(select avg(cast(HighestBidAmount as bigint)) from auction where ItemName like @ItemName and claimed = 1 and bin = 1 and datename(WEEKDAY, EndDate) = 'Tuesday') 
as Tuesday,
(select avg(cast(HighestBidAmount as bigint)) from auction where ItemName like @ItemName and claimed = 1 and bin = 1 and datename(WEEKDAY, EndDate) = 'Wednesday') 
as Wednesday,
(select avg(cast(HighestBidAmount as bigint)) from auction where ItemName like @ItemName and claimed = 1 and bin = 1 and datename(WEEKDAY, EndDate) = 'Thursday') 
as Thursday,
(select avg(cast(HighestBidAmount as bigint)) from auction where ItemName like @ItemName and claimed = 1 and bin = 1 and datename(WEEKDAY, EndDate) = 'Friday') 
as Friday,
(select avg(cast(HighestBidAmount as bigint)) from auction where ItemName like @ItemName and claimed = 1 and bin = 1 and datename(WEEKDAY, EndDate) = 'Saturday') 
as Saturday,
(select avg(cast(HighestBidAmount as bigint)) from auction where ItemName like @ItemName and claimed = 1 and bin = 1 and datename(WEEKDAY, EndDate) = 'Sunday') 
as Sunday
go

create procedure SelectWeekdayLowestBIN
@ItemName as nvarchar(255)
as
select 
(select min(HighestBidAmount) from auction where ItemName like @ItemName and claimed = 1 and bin = 1 and datename(WEEKDAY, EndDate) = 'Monday') 
as Monday,
(select min(HighestBidAmount) from auction where ItemName like @ItemName and claimed = 1 and bin = 1 and datename(WEEKDAY, EndDate) = 'Tuesday') 
as Tuesday,
(select min(HighestBidAmount) from auction where ItemName like @ItemName and claimed = 1 and bin = 1 and datename(WEEKDAY, EndDate) = 'Wednesday') 
as Wednesday,
(select min(HighestBidAmount) from auction where ItemName like @ItemName and claimed = 1 and bin = 1 and datename(WEEKDAY, EndDate) = 'Thursday') 
as Thursday,
(select min(HighestBidAmount) from auction where ItemName like @ItemName and claimed = 1 and bin = 1 and datename(WEEKDAY, EndDate) = 'Friday') 
as Friday,
(select min(HighestBidAmount) from auction where ItemName like @ItemName and claimed = 1 and bin = 1 and datename(WEEKDAY, EndDate) = 'Saturday') 
as Saturday,
(select min(HighestBidAmount) from auction where ItemName like @ItemName and claimed = 1 and bin = 1 and datename(WEEKDAY, EndDate) = 'Sunday') 
as Sunday
go

create procedure SelectWeekdayHighestBIN
@ItemName as nvarchar(255)
as
select 
(select max(HighestBidAmount) from auction where ItemName like @ItemName and claimed = 1 and bin = 1 and datename(WEEKDAY, EndDate) = 'Monday') 
as Monday,
(select max(HighestBidAmount) from auction where ItemName like @ItemName and claimed = 1 and bin = 1 and datename(WEEKDAY, EndDate) = 'Tuesday') 
as Tuesday,
(select max(HighestBidAmount) from auction where ItemName like @ItemName and claimed = 1 and bin = 1 and datename(WEEKDAY, EndDate) = 'Wednesday') 
as Wednesday,
(select max(HighestBidAmount) from auction where ItemName like @ItemName and claimed = 1 and bin = 1 and datename(WEEKDAY, EndDate) = 'Thursday') 
as Thursday,
(select max(HighestBidAmount) from auction where ItemName like @ItemName and claimed = 1 and bin = 1 and datename(WEEKDAY, EndDate) = 'Friday') 
as Friday,
(select max(HighestBidAmount) from auction where ItemName like @ItemName and claimed = 1 and bin = 1 and datename(WEEKDAY, EndDate) = 'Saturday') 
as Saturday,
(select max(HighestBidAmount) from auction where ItemName like @ItemName and claimed = 1 and bin = 1 and datename(WEEKDAY, EndDate) = 'Sunday') 
as Sunday
go

create procedure UpdateAuction
@claimed as bit,
@claimedBidders as nvarchar(255),
@highestBidAmount as int,
@uuid as nvarchar(255)
as
update Auction set Claimed = @claimed, ClaimedBidders = @claimedBidders, HighestBidAmount = @highestBidAmount where UUID = @uuid
go

create procedure InsertAuction
@uuid					nvarchar(255),
@auctioneer				nvarchar(255),
@profileID				nvarchar(255),
@startDate				DateTime2,
@endDate				DateTime2,
@itemName				nvarchar(255),
@itemLore				nvarchar(2555),
@extra					nvarchar(1000),
@category				nvarchar(255),
@tier					nvarchar(255),
@startingBid			int,
@itemBytes				nvarchar(2555),
@claimed				bit,
@claimedBidders			nvarchar(255),
@highestBidAmount		int,
@bin					bit
as
set transaction isolation level serializable;
begin transaction;
update Auction set uuid = @uuid, auctioneer = @auctioneer, profileID = @profileID, startDate =@startDate, endDate=@endDate , itemName=@itemName, 
itemLore = @itemLore, extra =@extra, category=@category, tier=@tier, startingBid=@startingBid, itemBytes= @itemBytes, claimed=@claimed, 
claimedBidders=@claimedBidders, highestBidAmount=@highestBidAmount, BIN=@bin where uuid = @uuid
if @@rowcount =0
begin
insert into Auction (uuid, auctioneer, profileID, startDate, endDate, itemName, itemLore, extra, category, tier, startingBid, itemBytes, claimed, claimedBidders, highestBidAmount, BIN) 
values (@uuid, @auctioneer, @profileID, @startDate, @endDate, @itemName, @itemLore, @extra, @category, @tier, @startingBid, @itemBytes, @claimed, @claimedBidders, @highestBidAmount, @bin)
end
commit transaction
go
							
create procedure InsertBid
@auctionID as nvarchar(255),
@profileID as nvarchar(255),
@bidder as nvarchar(255),
@timestamp as datetime2,
@bidAmount as int
as
if not exists (select * from Bid inner join BidToAuction on Bid.ID = BidToAuction.BidID where BidAmount= @bidAmount and AuctionID = @auctionID)
begin
insert into bid (ProfileId, Bidder, Timestamp, BidAmount) 
values (@profileID, @bidder, @timestamp, @bidAmount)
end
go

create procedure InsertBidToAuction
@bidID as nvarchar(255),
@auctionID as nvarchar(255)
as
insert into BidToAuction (BidID, AuctionID) 
values (@bidID, @auctionID)
go

create procedure SelectHourlyHighestBIN
@ItemName as nvarchar(255)
as
select datepart(hh, cast(EndDate as datetime)) AS hour,
            max(cast(HighestBidAmount as bigint)) AS average
from        Auction
where itemname like @ItemName and Claimed = 1 and BIN = 1
group by datepart(hh, cast(EndDate as datetime))
go

create procedure SelectHourlyLowestBIN
@ItemName as nvarchar(255)
as
select datepart(hh, cast(EndDate as datetime)) AS hour,
            min(cast(HighestBidAmount as bigint)) AS average
from        Auction
where itemname like @ItemName and Claimed = 1 and BIN = 1
group by datepart(hh, cast(EndDate as datetime))
go

create procedure SelectHourlyAverageBIN
@ItemName as nvarchar(255)
as
select datepart(hh, cast(EndDate as datetime)) AS hour,
            avg(cast(HighestBidAmount as bigint)) AS average
from        Auction
where itemname like @ItemName and Claimed = 1 and BIN = 1
group by datepart(hh, cast(EndDate as datetime))
go

create procedure SelectItemNameQuery
@ItemName as nvarchar(255)
as
select distinct(ItemName) from Auction where ItemName like @ItemName
go