using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace SPZC.Controllers {
    public class HomeController : Controller {

        private Random randomizer = new Random();
        private static string currentRandomizedValue = "";

        private string RandomizeSimple(string textToRandomize) {
            int randomizedInt = int.Parse(textToRandomize) + randomizer.Next(0, 10000);
            return randomizedInt.ToString();
        }
        private string DerandomizeSimple(string textToDerandomize) {
            int derandomizedInt = int.Parse(textToDerandomize) - randomizer.Next(0, 10000);
            return derandomizedInt.ToString();
        }

        public ActionResult Index() {
            return View();
        }

        public ActionResult About() {
            ViewBag.Message = "[HttpGet] About() was run";
            currentRandomizedValue = RandomizeSimple("123456");
            ViewBag.FormId = currentRandomizedValue;
            ViewBag.SubmittedValue = "not yet set";

            return View();
        }

        [HttpPost]
        public ActionResult About(FormCollection collection) {
            ViewBag.Message = "[HttpPost] About() was run";
            ViewBag.SubmittedValue = collection[currentRandomizedValue] + ", tag: " + currentRandomizedValue;
            currentRandomizedValue = RandomizeSimple("123456");
            ViewBag.FormId = currentRandomizedValue;

            return View();
        }

        public ActionResult Contact() {
            ViewBag.Message = "Your contact page.";

            return View();
        }

    }
}