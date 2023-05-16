
const http = require("http");
const url = require("url");
const port = 3000;
const Obs = require('./Obs');

obs = new Obs()

const svr = http.createServer((req,res)=>{
	if(req.url==="/"){
		obs.Root(res,'/');
	}else if(req.url==="/word"){
		obs.Word(res,'/word');
	}else{
		obs.NotFound(res);
	}
});

svr.listen(port,()=>{
	console.log(`Server listening on port ${port}`);
});
