const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");
const TerserPlugin = require('terser-webpack-plugin');

const basePath = `${__dirname}/bvspca`;

const config = function (env, argv) {
  const isProductionMode = argv.mode === 'production';
  return {
    entry: {
      project: `${basePath}/static/sass/project.scss`,
      bio: `${basePath}/core/js_src/bio.js`,
      site: `${basePath}/core/js_src/site.js`,
    },
    output: {
      path: `${basePath}/static/dist`,
      filename: '[name].js',
    },
    optimization: {
      minimizer: [
        new TerserPlugin({}),
        new CssMinimizerPlugin(),
      ],
      splitChunks: {
        chunks: 'all',
      },
    },
    module: {
      rules: [
        {
          test: /\.(js|jsx)$/,
          use: [
            {
              loader: 'babel-loader',
            },
          ],
        },
        {
          test: /\.scss$/,
          use: [
            {
              loader: MiniCssExtractPlugin.loader,
            },
            {
              loader: 'css-loader',
              options: {
                url: false,
              },
            },
            {
              loader: 'postcss-loader',
              options: {
                postcssOptions: {
                  plugins: [
                    'postcss-preset-env',
                  ],
                },
              },
            },
            {
              loader: 'sass-loader',
            },
          ],
        },
      ],
    },
    plugins: [
      new MiniCssExtractPlugin({
        filename: '[name].css',
        chunkFilename: '[id].css',
      }),
      new MiniCssExtractPlugin(),
    ],
  };
};

module.exports = config;
