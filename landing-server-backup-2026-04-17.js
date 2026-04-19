const http = require('http');
const fs = require('fs');
const path = require('path');

const root = path.join(__dirname, '02_MARKETING_ASSETS/marketing-foundation');
const port = 3457;

const mime = { '.html':'text/html', '.css':'text/css', '.js':'application/javascript', '.png':'image/png', '.jpg':'image/jpeg', '.svg':'image/svg+xml', '.json':'application/json', '.ttf':'font/ttf', '.woff2':'font/woff2' };

http.createServer((req, res) => {
  let filePath = path.join(root, req.url === '/' ? '/hypeshow-landing.html' : req.url);
  fs.readFile(filePath, (err, data) => {
    if (err) { res.writeHead(404); res.end('Not found'); return; }
    res.writeHead(200, { 'Content-Type': mime[path.extname(filePath)] || 'text/plain' });
    res.end(data);
  });
}).listen(port);
