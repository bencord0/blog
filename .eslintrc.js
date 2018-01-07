module.exports = {
    "env": {
        "browser": true,
        "es6": true,
        "jest/globals": true,
    },
    "extends": [
      "eslint:recommended",
      "plugin:react/recommended",
    ],
    "parserOptions": {
        "ecmaFeatures": {
            "experimentalObjectRestSpread": true,
            "jsx": true
        },
        "sourceType": "module"
    },
    "plugins": [
        "jest",
        "react",
    ],
    "rules": {
        "indent": [
            "error",
            2
        ],
        "linebreak-style": [
            "error",
            "unix"
        ],
        "no-console": "off",
        "no-unused-vars": ["error", {"args": "none"}],
        "padded-blocks": "off",
        "quotes": [
            "error",
            "double"
        ],
        "semi": [
            "error",
            "always"
        ],
        "react/prop-types": "off",
    }
};
