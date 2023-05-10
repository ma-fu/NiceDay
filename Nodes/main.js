const http = require("http");
const url = require("url");
const port = 3000;
function start(route,hand){
	const html = require("fs").readFileSync("./he.html")

	const svr = http.createServer((req,res)=>{
		const pathname = url.parse(req.url).pathname;
		console.log("Request for" + pathname +" received.");
		
		route(hand,pathname)

		res.writeHead(200,{"Content-Type":"text/html;charset=utf-8"});
		process.on("uncaughtException",(e) => console.log(e));
		res.end(html)
		console.log(`Sent a response : html`);
	});

	svr.listen(port)
	console.log(`The server has started and is listening on port number: ${port}`);
}

exports.start = start;
