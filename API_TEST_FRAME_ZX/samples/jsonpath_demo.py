import jsonpath

d1 = {
   "data" : {
      "testCaseData" : [
         {
            "agent_version" : "9.7.0.2225",
            "android_id" : "e3d699cf01620531",
            "asset_number" : "",
            "FILE" : "./ wwwccko(33)  .zip",
            "noncomp_reason" : "",
         },
         {
            "agent_version" : "2.0.0.1518",
            "android_id" : "",
            "asset_number" : "",
             "FILE" : "./XXXX(22)  .zip",
            "noncomp_reason" : "",
         }
      ],
      "total_count" : 2
   },
   "error_code" : 1,
   "message" : "Success",
   "timestamp" : 1504765848
}
value = jsonpath.jsonpath(d1,"$.data.testCaseData[0].agent_version")
print(value)