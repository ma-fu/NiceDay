function route(hand,pathname){
	console.log("About to route a request for " + pathname);
	if(typeof hand[pathname]==="function"){
		hand[pathname]();
	}else{
		console.log("No request handler found for"+pathname);
	}
}
exports.route=route;
