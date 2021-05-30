using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using SPZC.Models;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;



namespace SPZC.Controllers
{
    public class HomeController : Controller
    {
        private Random randomizer = new Random();
        private static string currentRandomizedfnameValue = "";
        private static string currentRandomizedlnameValue = "";

        private string RandomizeSimple(string textToRandomize) {
            int randomizedInt = int.Parse(textToRandomize) + randomizer.Next(0, 10000);
            return randomizedInt.ToString();
        }
        private string DerandomizeSimple(string textToDerandomize) {
            int derandomizedInt = int.Parse(textToDerandomize) - randomizer.Next(0, 10000);
            return derandomizedInt.ToString();
        }

        public ActionResult Index() {
            ViewBag.Message = "[HttpGet] method was run.";
            currentRandomizedfnameValue = RandomizeSimple("123456");
            ViewBag.fnameID = currentRandomizedfnameValue;
            currentRandomizedlnameValue = RandomizeSimple("123456");
            ViewBag.lnameID = currentRandomizedlnameValue;
            ViewBag.SubmittedValue = "not yet set";

            return View();
        }

        [HttpPost]
        public ActionResult Index(IFormCollection collection) {
            ViewBag.Message = "[HttpPost] method was run.";
            ViewBag.SubmittedValue = collection[currentRandomizedfnameValue] + ", " + collection[currentRandomizedlnameValue] + ". Ids used in previous form: " + currentRandomizedfnameValue + ", " + currentRandomizedlnameValue;
            currentRandomizedfnameValue = RandomizeSimple("123456");
            ViewBag.fnameID = currentRandomizedfnameValue;
            currentRandomizedlnameValue = RandomizeSimple("123456");
            ViewBag.lnameID = currentRandomizedlnameValue;

            return View();
        }
    }
}
