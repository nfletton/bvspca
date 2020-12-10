const autoprefixer = require('autoprefixer');
const cssnano = require('cssnano');
const path = require('path');
const postCssFlexbugsFixes = require('postcss-flexbugs-fixes');
const webpack = require('webpack');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

const basePath = `${__dirname}/bvspca`;

const config = function () {
  return {
    entry: {
      sass: `${basePath}/static/sass/project.scss`,
      bio: `${basePath}/core/js_src/bio.js`,
      site: `${basePath}/core/js_src/site.js`,
    },
    output: {
      path: `${basePath}/static/dist`,
      filename: '[name].js',
    },
    module: {
      rules: [
        {
          test: /\.(js|jsx)$/,
          use: [
            {
              loader: 'babel-loader',
              options: {
                presets: ['es2015'],
              },
            },
          ],
          exclude: /(node_modules|bower_components)/,
        },
        {
          test: /\.scss$/,
          use: ExtractTextPlugin.extract({
            use: [
              // {loader: 'style-loader'},
              {
                loader: 'css-loader',
                options: { url: false, sourceMap: true },
              },
              {
                loader: 'postcss-loader',
                options: {
                  plugins: () => {
                    const cssPlugins = [
                      postCssFlexbugsFixes,
                      autoprefixer(),
                    ];
                    if (process.env.NODE_ENV === 'production') {
                      cssPlugins.push(cssnano);
                    }
                    return cssPlugins;
                  },
                  sourceMap: true,
                },
              },
              {
                loader: 'sass-loader',
                options: {
                  sourceMap: true,
                },
              },
            ],
          }),
        },
      ],
    },
    plugins: [
      new ExtractTextPlugin('project.css'),
    ],
  };
};

module.exports = config;
