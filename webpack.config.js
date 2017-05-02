var path = require('path');

module.exports = {
  entry: 'app/static/components.jsx',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'app/static')
  }
};
