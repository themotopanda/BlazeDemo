import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

class BZD_Test extends Simulation {
  val concurrency = Integer.getInteger("concurrency", 100).toInt
  val rampUpTime = Integer.getInteger("ramp-up", 10).toInt
  val holdForTime = Integer.getInteger("hold-for", 60).toInt
  val throughput = Integer.getInteger("throughput")
  val iterationLimit = Integer.getInteger("iterations")

  val httpConf = http
    .baseURL("http://www.blazedemo.com")

  val durationLimit = rampUpTime + holdForTime
  val scn = scenario("Blazedemo").forever() {
    exec(http("Home").get("/"))
    .exec(http("Reserve").get("/reserve.php"))
    .exec(http("Purchase").get("/purchase.php"))
    .exec(http("Confirmation").get("/confirmation.php"))
  }
  val execution = scn
    .inject(rampUsers(concurrency) over rampUpTime)
    .protocols(httpConf)

  setUp(execution).maxDuration(rampUpTime + holdForTime)
  }