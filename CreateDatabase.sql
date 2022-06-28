drop table if exists Bid;
drop table if exists BidToAuction;
drop table if exists Auction;

drop database if exists SkyAuctionsDB;

create database SkyAuctionsDB;

use SkyAuctionsDB;

create table Bid(
	ID int primary key not null IDENTITY(1,1),
	ProfileID varchar(255),
	Bidder varchar(255),
	Timestamp datetime2,
	BidAmount int
)

create table BidToAuction(
	BidID int,
	AuctionID varchar(255),
	primary key (BidID, AuctionID)
)

create table Auction(
	BIN					bit,
	UUID				varchar(255) primary key,
	Auctioneer			varchar(255),
	ProfileID			varchar(255),
	StartDate			DateTime2,
	EndDate				DateTime2,
	ItemName			varchar(255),
	ItemLore			varchar(2555),
	Extra				varchar(1000),
	Category			varchar(155),
	Tier				varchar(155),
	StartingBid			int,
	ItemBytes			varchar(2555),
	Claimed				bit,
	ClaimedBidders		varchar(255),
	HighestBidAmount	int,	
)

create unique index AuctionUUID on Auction(uuid);