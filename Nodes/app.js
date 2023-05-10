const svr = require("./main");
const rts = require("./router");
const handler = require("./Hand");

const hand = {}

hand["/"] = handler.start;
hand["/start"] = handler.start;
hand["/upload"] = handler.upload;

svr.start(rts.route,hand);
