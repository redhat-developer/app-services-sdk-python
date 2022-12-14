const fs = require("fs");
const { cwd } = require("process");
const apis = require(cwd() + "/.errors/index.js");

console.log("Generating errors sdks");

for (api in apis) {
  console.log("Generating error SDK for " + api);
  apiJson = apis[api].definition;
  apiFileLocation = apis[api].file;

  if (!apiJson || !apiJson.items) {
    console.log("invalid error file detected", apiJson);
    exit(1);
  }

  stringBuffer = 
`from enum import Enum 

#   ${api} error codes

class APIErrorCodes(Enum):
`;

  apiJson.items.forEach(function (errorType) {
    stringBuffer += `  # ${errorType.reason} \n`;
    stringBuffer += `  ERROR_${errorType.id} = "${errorType.code}" \n\n`;
  });


  fs.writeFileSync(
    cwd() + "/" + apiFileLocation, stringBuffer, { encoding: "utf8" });
  console.log(`Sucessfully generated ${api} error definitions`);
}
