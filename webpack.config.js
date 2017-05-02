var path = require('path');

module.exports = {
  entry: path.join(__dirname, 'app/static/js/test.jsx'),
  output: {
    filename: 'bundle.js',
    path: path.join(__dirname, 'app/static/js')
  },
  module: {
    rules: [
      {
        test: /\.jsx$/,
        exclude: /node_modules/,
        use: 'babel-loader'
      }
    ]
  }
};
