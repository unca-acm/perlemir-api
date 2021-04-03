import React from "react";
import { Grid, Box } from "@chakra-ui/react";

import { BotInstance } from "../bot/BotInstance";
import BotControlPanel from "../bot/BotControlPanel";
import BotCardDCA from "../bot/dca/BotCardDCA";
import * as BotDCA from "../bot/dca/BotDCA";

interface DashboardProps {
    plotSize: { width: number, height: number };
}

const Dashboard: React.FC<DashboardProps> = function(props) {
    const [ botInstances, setBotInstances ] = React.useState<{ [id: string]: BotInstance<unknown> }>({});

    return (
        <Grid backgroundColor="white" id="app-grid" templateColumns="60% 40%">
            <Box w="100%" p={0}
                display="flex"
                flexFlow="column"
                borderWidth="2px"
                borderColor="perlemirBrand.100"
                overflow="hidden"
                minHeight="400px"
                maxHeight="600px"
                borderRadius="20px 20px 0 0"
            >
                <Box flex="0 1 auto">
                    <BotControlPanel
                        onCreate={instance => {
                            setBotInstances({ [instance.id]: instance, ...botInstances });
                        }}
                    />
                </Box>
                <Box flex="1 1 auto" overflow="scroll">
                    {Object.keys(botInstances).length > 0 ? Object.values(botInstances).map(instance => (
                        <BotCardDCA
                            key={instance.id}
                            instance={instance as BotDCA.Instance}
                            dispatch={val => {
                                Object.assign(botInstances[instance.id], val);
                                setBotInstances({ ...botInstances });
                            }}
                        />
                    )) : (
                        <div>
                            <h1 style={{ color: "black" }}>No bots active</h1>
                        </div>
                    )}
                </Box>
            </Box>
        </Grid>
    );
};

export default Dashboard;
