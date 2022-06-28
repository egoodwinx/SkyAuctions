//https://github.com/FoxInFlame/MinecraftColorCodes
var obfuscators = [];
var styleMap = {
    '§4': 'font-weight:normal;text-decoration:none;color:#be0000',
    '§c': 'font-weight:normal;text-decoration:none;color:#fe3f3f',
    '§6': 'font-weight:normal;text-decoration:none;color:#d9a334',
    '§e': 'font-weight:normal;text-decoration:none;color:#fefe3f',
    '§2': 'font-weight:normal;text-decoration:none;color:#00be00',
    '§a': 'font-weight:normal;text-decoration:none;color:#3ffe3f',
    '§b': 'font-weight:normal;text-decoration:none;color:#3ffefe',
    '§3': 'font-weight:normal;text-decoration:none;color:#00bebe',
    '§1': 'font-weight:normal;text-decoration:none;color:#0000be',
    '§9': 'font-weight:normal;text-decoration:none;color:#3f3ffe',
    '§d': 'font-weight:normal;text-decoration:none;color:#fe3ffe',
    '§5': 'font-weight:normal;text-decoration:none;color:#be00be',
    '§f': 'font-weight:normal;text-decoration:none;color:#ffffff',
    '§7': 'font-weight:normal;text-decoration:none;color:#bebebe',
    '§8': 'font-weight:normal;text-decoration:none;color:#3f3f3f',
    '§0': 'font-weight:normal;text-decoration:none;color:#000000',
    '§l': 'font-weight:bold',
    '§n': 'text-decoration:underline;text-decoration-skip:spaces',
    '§o': 'font-style:italic',
    '§m': 'text-decoration:line-through;text-decoration-skip:spaces',
};
function obfuscate(string, elem) {
    var magicSpan,
        currNode,
        len = elem.childNodes.length;
    if(string.indexOf('<br>') > -1) {
        elem.innerHTML = string;
        for(var j = 0; j < len; j++) {
            currNode = elem.childNodes[j];
            if(currNode.nodeType === 3) {
                magicSpan = document.createElement('span');
                magicSpan.innerHTML = currNode.nodeValue;
                elem.replaceChild(magicSpan, currNode);
                init(magicSpan);
            }
        }
    } else {
        init(elem, string);
    }
    function init(el, str) {
        var i = 0,
            obsStr = str || el.innerHTML,
            len = obsStr.length;
        obfuscators.push( window.setInterval(function () {
            if(i >= len) i = 0;
            obsStr = replaceRand(obsStr, i);
            el.innerHTML = obsStr;
            i++;
        }, 0) );
    }
    function randInt(min, max) {
        return Math.floor( Math.random() * (max - min + 1) ) + min;
    }
    function replaceRand(string, i) {
        var randChar = String.fromCharCode( randInt(64,90) ); /*Numbers: 48-57 Al:64-90*/
        return string.substr(0, i) + randChar + string.substr(i + 1, string.length);
    }
}
function applyCode(string, codes) {
    var len = codes.length;
    var elem = document.createElement('span'),
        obfuscated = false;
    for(var i = 0; i < len; i++) {
        elem.style.cssText += styleMap[codes[i]] + ';';
        if(codes[i] === '§k') {
            obfuscate(string, elem);
            obfuscated = true;
        }
    }
    if(!obfuscated) elem.innerHTML = string;
    return elem;
}
function parseStyle(string) {
    var codes = string.match(/§.{1}/g) || [],
        indexes = [],
        apply = [],
        tmpStr,
        indexDelta,
        noCode,
        final = document.createDocumentFragment(),
        len = codes.length,
        string = string.replace(/\n|\\n/g, '<br>');
    
    for(var i = 0; i < len; i++) {
        indexes.push( string.indexOf(codes[i]) );
        string = string.replace(codes[i], '\x00\x00');
    }
    if(indexes[0] !== 0) {
        final.appendChild( applyCode( string.substring(0, indexes[0]), [] ) );
    }
    for(var i = 0; i < len; i++) {
    	indexDelta = indexes[i + 1] - indexes[i];
        if(indexDelta === 2) {
            while(indexDelta === 2) {
                apply.push ( codes[i] );
                i++;
                indexDelta = indexes[i + 1] - indexes[i];
            }
            apply.push ( codes[i] );
        } else {
            apply.push( codes[i] );
        }
        if( apply.lastIndexOf('§r') > -1) {
            apply = apply.slice( apply.lastIndexOf('§r') + 1 );
        }
        tmpStr = string.substring( indexes[i], indexes[i + 1] );
        final.appendChild( applyCode(tmpStr, apply) );
    }
    return final;
}
function clearObfuscators() {
    var i = obfuscators.length;
    for(;i--;) {
        clearInterval(obfuscators[i]);
    }
    obfuscators = [];
}
String.prototype.replaceColorCodes = function() {
  clearObfuscators();
  var outputString = parseStyle(String(this));
  return outputString;
};

/////////////////////////////////////////////////
function cutString(str, cutStart, cutEnd){
  return str.substr(0,cutStart) + str.substr(cutEnd+1);
}

function parseHypixelText(text)
{
    return new XMLSerializer().serializeToString(text.toString().replace(/\?/g, "✪").replaceColorCodes())
}

function generateAuctionDisplay(auction){
    const outer = createElement('div', 'col-sm-3');
    outer.style.marginBottom = "10px";
    const div = createElement('div', 'card')
    div.id = auction.uuid
    div.style.backgroundColor= "#696969"
    const cardTitle = createElement('h5', 'card-title');
    cardTitle.innerHTML = parseHypixelText(auction.itemname);
    div.append(cardTitle);  
    //colour the card title based on the type
    if (auction.tier === "LEGENDARY"){
        cardTitle.style.color = "#FFAA00"
    } 
    else if (auction.tier === "UNCOMMON"){
        cardTitle.style.color ="#55FF55";
    }
    else if (auction.tier === "COMMON"){
        cardTitle.style.color = "#FFFFFF"
    }
    else if (auction.tier === "RARE"){
        cardTitle.style.color= "#0000AA"
    }
    else if (auction.tier === "EPIC"){
        cardTitle.style.color = "#AA00AA";
    }
    else if (auction.tier === "MYTHIC"){
        cardTitle.style.color = "#FF55FF";
    }
    else if (auction.tier === "DIVINE"){
        cardTitle.style.color = "#55FFFF";
    }
    else if (auction.tier === "SPECIAL"){
        cardTitle.style.color = "#FF5555";
    }
    else if (auction.tier === "VERY SPECIAL"){
        cardTitle.style.color = "#FF5555";
    }

    if (auction.bin === false){
        const startingBid = createElement("h6");
        startingBid.style.textAlign = "center";
        startingBid.textContent = "Starting Bid: " + auction.startingbid;
        const currentBid = createElement("h6");
        currentBid.style.textAlign = "center";
        if (auction.highestbidamount == 0){
            currentBid.textContent = "Current Bid: No Bids";
        }
        else{
            currentBid.textContent = "Current Bid: " + auction.highestbidamount;
        }
        div.append(startingBid, currentBid);
    }
    else {
        const bin = createElement("h6");
        bin.style.textAlign = "center";
        bin.textContent = "BIN for: " + auction.startingbid;
        div.append(bin);
    }
    const collapsable = createElement('div', 'collapse')
    collapsable.classList.add("multi-collapse");
    collapsable.id = "collapse_" + auction.uuid;
    const innerDiv = createElement('div', 'card-body')
    innerDiv.innerHTML = parseHypixelText(auction.itemlore);
    const expand = createElement('button', 'btn')
    expand.setAttribute("type", "button")
    expand.classList.add("btn")
    expand.setAttribute("data-bs-toggle", "collapse")
    expand.setAttribute("data-bs-target", "#collapse_"+auction.uuid)
    expand.ariaExpanded = false;
    expand.setAttribute("aria-controls", auction.uuid + "Collapse");
    expand.textContent = "Expand..."
    collapsable.append(innerDiv);
    div.append(collapsable, expand);               
    outer.append(div);
    return outer;
}

// Create an element with an optional CSS class
function createElement(tag, className) {
    const element = document.createElement(tag);
    if (className) element.classList.add(className);

    return element;
}

// Retrieve an element from the DOM
function getElement(selector) {
    const element = document.querySelector(selector)

    return element
}

// create dropdown element
function createDropDown(btnID, labelText, dropdownItems){
    const binDiv = createElement('div', 'col-auto');
    const label = createElement('label', 'col-form-label');
    label.textContent = labelText;
    binDiv.append(label);   
    const select = createElement('select', 'form-select');
    select.setAttribute('aria-label', 'Select BIN Type');
    select.id = btnID;
    for (var i = 0; i < dropdownItems.length; i++) {
        const item = createElement('option', 'dropdown-item');
        item.textContent = dropdownItems[i];
        select.append(item);
    }
    binDiv.append(select);
    return binDiv;
}