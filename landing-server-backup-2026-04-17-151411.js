const http = require('http');
const fs = require('fs');
const path = require('path');

const root = path.join(__dirname, '02_MARKETING_ASSETS/marketing-foundation');
const langRoot = path.join(__dirname, 'Languages');
const port = 3457;

const mime = { '.html':'text/html', '.css':'text/css', '.js':'application/javascript', '.png':'image/png', '.jpg':'image/jpeg', '.svg':'image/svg+xml', '.json':'application/json', '.ttf':'font/ttf', '.woff2':'font/woff2' };

http.createServer((req, res) => {
  const url = req.url.split('?')[0];
  let filePath;
  if (url.startsWith('/Languages/')) {
    filePath = path.join(langRoot, url.slice('/Languages/'.length));
  } else {
    filePath = path.join(root, url === '/' ? '/hypeshow-landing.html' : url);
  }
  fs.readFile(filePath, (err, data) => {
    if (err) { res.writeHead(404); res.end('Not found'); return; }
    const headers = { 'Content-Type': mime[path.extname(filePath)] || 'text/plain' };
    if (path.extname(filePath) === '.json') headers['Access-Control-Allow-Origin'] = '*';
    res.writeHead(200, headers);
    res.end(data);
  });
}).listen(port);
