
const http = require("http");
const url = require("url");
const port = 3000;
const tmpGen = require('./tmp');
const Obs = require('./Obs');

obs = new Obs()

const svr = http.createServer(async (req,res)=>{
	if(req.url==="/"){
		rows = await obs.alldata()
		html = tmpGen(rows)
		res.writeHead(200,{'Content-Type':'text/html'});
		res.end(html);
	/*
		if(er){
			res.writeHead(500,{"Content-Type":"text/plain"});
			res.end("Internal Server Error");
		}else{
			res.writeHead(200,{"Content-Type":"text/html"});
			res.end(html);
			}
		});
	*/
	}else{
		res.writeHead(404,{"Content-Type":"text/plain"});
		res.end("Not Found");
	}
});

svr.listen(port,()=>{
	console.log(`Server listening on port ${port}`);
});
