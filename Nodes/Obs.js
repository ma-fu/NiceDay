const sqlite3 = require("sqlite3");

class Obs {
	constructor(){
		this.adb = './AWSdb';
		this.slal = 'select * from areas';
	}

	alldata(){
		return new Promise((resolve,reject)=>{
			const db = new sqlite3.Database(this.adb);
			db.all(this.slal,(er,rows)=>{
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
