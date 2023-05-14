function tmpGen(rows){
	const Table = `
		<table>
			<thead>
				<tr>
					<th>ID</th>
					<th>Area</th>
				</tr>
			</thead>
			<tbody>
			 ${rows
			 .map((row)=>`<tr><td>${row.id}</td><td>${row.area}</td></tr>`)
			 .join('')}
			 </tbody>
		 </table>
			 `;
	const html = `
		<!DOCTYPE html>
		<html>
		<head>
		<meta charset='utf-8'/>
		<title>User List</title>
		<style>
		table{
			border-collapse:collapse;
			width:100%;
		}
		th,td{
			border:1px solid #ddd;
			padding:8px;
			}
			</style>
		</head>
		<body>
		<h1>Area List</h1>
		${Table}
		</body>
		</html>
		`;
	return html;
}

module.exports = tmpGen;
