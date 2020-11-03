module.exports = {
    mode: 'development',
    module: {
        rules: [
            {
                test: /\.jsx?$/,
                loader: 'babel-loader'
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            },
            {
                test: /\.(png|jpg|jpeg|JPG)$/,
                loader: 'file-loader'
            }
        ]
    },
    devServer: {
        contentBase: 'dist',
        port: 3000
    }
}