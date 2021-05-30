/*using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;

    namespace SPZC.Models
    {
        public class Randomizer
        {
            public Dictionary<string, string> Randomize(string masterKey, string[] parameters)
            {
                string clientSessionKey = GetSessionKey(masterKey);
                Dictionary<string, string> randomizedDict = new Dictionary<string, string>();
                foreach(string param in parameters)
                {
                    randomizedDict[param] = RandomizeStr(param, clientSessionKey);
                }
                return randomizedDict;
            }


            public Dictionary<string, string> Derandomize(string masterKey, string[] taggedParameters)
            {

            }

            private string RandomizeStr(string parameter, string clientSessionKey)
            {

            }

            private string GetSessionKey(string masterKey)
            {
                HttpSessionState.SessionID
            }
        }
    }

*/