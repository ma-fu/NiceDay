class Tmpgen {
	constructor(rows,clms,usr){
		this.rows = rows;
		this.clms = clms;
		this.usr = usr;
	}
	Main(){
		return `
			<!DOCTYPE html>
			<html>
			<head>
			<meta charset='utf-8'/>
			<title>Areas List</title>
				${this.Style()}
			</head>
			<body>
			<h1>Areas List</h1>
				${this.Tbltmp()}
			</body>
			</html>
			`;
	}
	Tbltmp(){
		return `
			<table>
			<thead>
			<tr>
				${this.Clmstmp()}
			</tr>
			</thead>
			<tbody>
				${this.RowsL()}
			 </tbody>
			 </table>
				 `;
	}
	RowsL(){
		if(this.usr==='/'){
			return this.rows.map((row)=>`<tr><td>${row.id}</td><td>${row.area}</td></tr>`).join('');
		}else{
			return this.rows.map((row)=>`<tr><td>${row.id}</td><td>${row.word}</td><td>${row.desc}</td><td>${row.prac_id}</td></tr>`).join('');
		}
	}
	Clmstmp(){
		return this.clms.map((clm)=>`<th>${clm.name}</th>`).join('');
	}
	Style(){
		return `
			<style>
			table{
				border-collapse:collapse;
				width:100%;
			}
			th,td{
				border:1px solid #ddd;
				padding:8px;
			}
			</style>`;
	}

}

module.exports = Tmpgen;
