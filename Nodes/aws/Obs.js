const sqlite3 = require("sqlite3");
const Tmpgen = require('./tmp');
const util = require('util');


class Obs {
	constructor(){
		this.adb = './AWSdb';
	}
	
	InternalServerError(res){
		res.writeHead(500,{"Content-Type":"text/plain"});
		res.end("Internal Server Error");
	}

	NotFound(res){
		res.writeHead(404,{"Content-Type":"text/plain"});
		res.end("Not Found");
	}

	async Root(res,r){
		let q = 'select * from areas';
		const rows = await this.alldata(q);
		q = 'PRAGMA table_info(Areas)';
		const cls = await this.alldata(q);
		const tmp = new Tmpgen(rows,cls,r);
		res.writeHead(200,{'Content-Type':'text/html'});
		res.end(tmp.Main());
	}
	async Word(res,r){
		let q = 'select * from awskyws';
		const rows = await this.alldata(q); 
		q = 'PRAGMA table_info(awskyws)';
		const cls = await this.alldata(q);
		const tmp = new Tmpgen(rows,cls,r);
		res.writeHead(200,{'Content-Type':'text/html'});
		res.end(tmp.Main());
	}

	alldata(q){
		return new Promise((resolve,reject)=>{
			const db = new sqlite3.Database(this.adb);
			db.all(q,(er,rows)=>{
				if(er){
					reject(er);
				}else{
					resolve(rows);
				}
			});
			db.close();
		});
	}
}

module.exports = Obs;
