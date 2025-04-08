const zonPrettierConfig = require('@zeitonline/prettier-config');

/**
 * Note: this picks up the .editorconfig and overrides/extends it.
 * The .editorconfig that should be used can be found at:
 * https://github.com/ZeitOnline/frontend-code-style/blob/main/.editorconfig
 *
 * @type {import('prettier').Options}
 */
module.exports = {
	...zonPrettierConfig,
};
