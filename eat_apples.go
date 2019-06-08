package main

import (
	"fmt"
	"sort"
	"time"

	"github.com/tebeka/selenium"
)

const (
	port = 8080
)

func main() {
	opts := []selenium.ServiceOption{}

	service, err := selenium.NewChromeDriverService("chromedriver", port, opts...)
	if err != nil {
		panic(err)
	}
	defer service.Stop()

	caps := selenium.Capabilities{"browserName": "chrome"}
	wd, err := selenium.NewRemote(caps, fmt.Sprintf("http://127.0.0.1:%d/wd/hub", port))
	if err != nil {
		panic(err)
	}
	defer wd.Quit()

	wd.Get("http://game.hg0355.com/game/xpg/?from=timeline&isappinstalled=0")

	time.Sleep(1 * time.Second)

	ready, _ := wd.FindElement(selenium.ByID, "ready-btn")
	ready.Click()

	for {
		score_button, _ := wd.FindElements(selenium.ByXPATH, "//div[(contains(@class, 't1') or contains(@class, 't2') or contains(@class, 't3') or contains(@class, 't4') or contains(@class, 't5')) and not(contains(@class, 'tt'))]")

		var locations = make(map[int]int)
		for i := 0; i < len(score_button); i++ {
			var location *selenium.Point
			location, _ = score_button[i].Location()
			locations[location.Y] = i
		}

		start = time.Now()
		var keys = make([]int, 0, len(locations))
		for k := range locations {
			keys = append(keys, k)
		}
		sort.Sort(sort.Reverse(sort.IntSlice(keys)))

		for _, k := range keys {
			location_index := locations[k]
			btn := score_button[location_index]
			is_enabled, _ := btn.IsEnabled()
			if is_enabled {
				btn.Click()
			}
		}
	}
}
