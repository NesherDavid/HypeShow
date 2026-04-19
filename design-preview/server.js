const http = require('http');
const fs = require('fs');
const path = require('path');

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.js':   'application/javascript',
  '.css':  'text/css',
  '.png':  'image/png',
  '.jpg':  'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp',
  '.svg':  'image/svg+xml',
};

const server = http.createServer((req, res) => {
  if (req.url === '/open-folder') {
    const { exec } = require('child_process');
    exec('open /Users/nesher/Desktop/HypeShow');
    res.writeHead(200, {'Content-Type':'application/json'});
    res.end(JSON.stringify({ok:true}));
    return;
  }

  // Serve static files from __dirname
  const urlPath = req.url.split('?')[0];
  const filePath = urlPath === '/' ? path.join(__dirname, 'index.html')
                                   : path.join(__dirname, urlPath);

  // Security: prevent path traversal
  if (!filePath.startsWith(__dirname)) {
    res.writeHead(403); res.end('Forbidden'); return;
  }

  const ext = path.extname(filePath).toLowerCase();
  fs.readFile(filePath, (err, data) => {
    if (err) {
      // Fallback to index.html for unknown routes
      fs.readFile(path.join(__dirname, 'index.html'), (e2, d2) => {
        if (e2) { res.writeHead(500); res.end('Error'); return; }
        res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
        res.end(d2);
      });
      return;
    }
    res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream' });
    res.end(data);
  });
});

server.listen(3456, () => console.log('Design preview running on port 3456'));
