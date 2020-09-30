// run with `./node_modules/.bin/mocha test.js`
const axios = require('axios').default;
const chai = require('chai');
const expect = chai.expect;
const chaiResponseValidator = require('chai-openapi-response-validator');
chai.use(chaiResponseValidator(__dirname + '/api.yaml'));
describe('foo', function() {
    it('should satisfy OpenAPI spec', async function() {
        this.timeout(3600000);
        // const res = await axios.get('http://localhost:9090/app/structure');
        const res = await axios.get('http://localhost:9090/app/cp/foo');
        expect(res).to.satisfyApiSpec;
    });
});
