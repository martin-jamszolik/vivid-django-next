module.exports = {
    trailingSlash: true,
    async rewrites() {
      return [
        {
          source: '/api/:path*/',
          destination: 'http://localhost:8000/api/:path*/', // Matched parameters can be used in the destination
        },
      ]
    },
  }
