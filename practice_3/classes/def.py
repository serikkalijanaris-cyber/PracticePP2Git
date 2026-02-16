<!DOCTYPE html>
<!-- saved from url=(0092)https://github.com/khavadim1-cyber/pp2_v_kha/blob/main/practise3/classes/class_defenition.py -->
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark" data-a11y-animated-images="system" data-a11y-link-underlines="true" class="js-focus-visible" data-js-focus-visible="" data-turbo-loaded=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style type="text/css">.turbo-progress-bar {
  position: fixed;
  display: block;
  top: 0;
  left: 0;
  height: 3px;
  background: #0076ff;
  z-index: 2147483647;
  transition:
    width 300ms ease-out,
    opacity 150ms 150ms ease-in;
  transform: translate3d(0, 0, 0);
}
</style><style>
:root {
  --fontStack-monospace: "Monaspace Neon", ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace !important;
}
</style>




  
    
  
  
  
  
  
  

  

  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./def_files/light-f30be7a1f27bcb6b.css"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./def_files/dark-d9d99f8c9aa4fbfd.css"><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-10373d2d112fc873.css"><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-d0145171d79f94f6.css"><link data-color-theme="light_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind_high_contrast-1d2d2c4ffae648c4.css"><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-11d6568044aeceeb.css"><link data-color-theme="light_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia_high_contrast-c38f22a98f01b293.css"><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-f68e181a9067f808.css"><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-c21a8c43bc3127eb.css"><link data-color-theme="dark_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind_high_contrast-635d755c05590766.css"><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-1abfbdc43c9465f6.css"><link data-color-theme="dark_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia_high_contrast-5d5617ce453e2abb.css"><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-9b6e5c8b7f02f5ae.css"><link data-color-theme="dark_dimmed_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed_high_contrast-1f2aa99a70f49a4b.css">

  <style type="text/css">
    :root {
      --tab-size-preference: 4;
    }

    pre, code {
      tab-size: var(--tab-size-preference);
    }
  </style>

    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./def_files/primer-primitives-f9161d06200ae2dc.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./def_files/primer-0b53c3bf3393e2ed.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./def_files/global-6326a07d26552848.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./def_files/github-c53b912064ef8de5.css">
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./def_files/repository-90ec7ed0aced8b41.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./def_files/code-6756960bc12d5d38.css">

  

  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["a11y_status_checks_ruleset","action_yml_language_service","actions_custom_images_public_preview_visibility","actions_custom_images_storage_billing_ui_visibility","actions_enable_snapshot_keyword","actions_image_version_event","actions_workflow_language_service","actions_workflow_language_service_allow_case_function","agent_session_retry_fetch_capi_on_401","alternate_user_config_repo","api_insights_show_missing_data_banner","arianotify_comprehensive_migration","batch_suggested_changes","billing_hard_budget_limits_for_licenses","billing_ui_budget_pagination_enabled","code_view_canvas_text_measurement","codeowners_validation_in_diff","codespaces_prebuild_region_target_update","coding_agent_model_selection","copilot_3p_agent_hovercards","copilot_agent_sessions_alive_updates","copilot_agent_task_list_v2","copilot_agent_task_submit_with_modifier","copilot_agent_tasks_btn_code_nav","copilot_agent_tasks_btn_code_view","copilot_agent_tasks_btn_code_view_lines","copilot_agent_tasks_btn_repo","copilot_api_agentic_issue_marshal_yaml","copilot_ask_mode_dropdown","copilot_capi_error_response_telemetry","copilot_chat_attach_multiple_images","copilot_chat_clear_model_selection_for_default_change","copilot_chat_disable_model_picker_while_streaming","copilot_chat_enable_tool_call_logs","copilot_chat_file_redirect","copilot_chat_input_commands","copilot_chat_opening_thread_switch","copilot_chat_reduce_quota_checks","copilot_chat_repository_picker","copilot_chat_search_bar_redirect","copilot_chat_selection_attachments","copilot_chat_vision_in_claude","copilot_chat_vision_preview_gate","copilot_coding_agent_free_users_exp","copilot_coding_agent_task_response","copilot_custom_copilots","copilot_custom_copilots_feature_preview","copilot_duplicate_thread","copilot_extensions_hide_in_dotcom_chat","copilot_extensions_removal_on_marketplace","copilot_features_raycast_logo","copilot_features_sql_server_logo","copilot_features_zed_logo","copilot_file_block_ref_matching","copilot_ftp_hyperspace_upgrade_prompt","copilot_icebreakers_experiment_dashboard","copilot_icebreakers_experiment_hyperspace","copilot_immersive_job_result_preview","copilot_immersive_structured_model_picker","copilot_immersive_task_hyperlinking","copilot_immersive_task_within_chat_thread","copilot_issue_list_show_more","copilot_mc_cli_resume_any_users_task","copilot_org_policy_page_focus_mode","copilot_premium_request_quotas","copilot_redirect_header_button_to_agents","copilot_share_active_subthread","copilot_spaces_ga","copilot_spaces_individual_policies_ga","copilot_spaces_pagination","copilot_spaces_server_side_menu_actions","copilot_spark_empty_state","copilot_spark_handle_nil_friendly_name","copilot_stable_conversation_view","copilot_swe_agent_use_subagents","copilot_unconfigured_is_inherited","custom_instructions_file_references","custom_properties_consolidate_default_value_input","dashboard_indexeddb_caching","dashboard_lists_max_age_filter","dashboard_universe_2025","dashboard_universe_2025_feedback_dialog","disable_turbo_visit","dom_node_counts","enterprise_ai_controls","failbot_report_error_react_apps_on_page","fgpat_permissions_selector_redesign","file_finder_skip_debounce","flex_cta_groups_mvp","global_nav_react","hide_groups_list_for_few_groups","hyperspace_2025_logged_out_batch_1","hyperspace_2025_logged_out_batch_2","initial_per_page_pagination_updates","issue_fields_global_search","issue_fields_report_usage","issue_fields_timeline_events","issues_cca_assign_actor_with_agent","issues_dashboard_inp_optimization","issues_expanded_file_types","issues_index_semantic_search","issues_lazy_load_comment_box_suggestions","issues_react_auto_retry_on_error","issues_react_bots_timeline_pagination","issues_react_chrome_container_query_fix","issues_react_custom_hpc_metric","issues_react_include_bots_in_pickers","issues_react_low_quality_comment_warning","issues_react_prohibit_title_fallback","issues_react_resource_metrics","issues_react_safari_scroll_preservation","issues_react_ui_feedback","issues_react_use_turbo_for_cross_repo_navigation","landing_pages_ninetailed","lifecycle_label_name_updates","marketing_pages_search_explore_provider","memex_default_issue_create_repository","memex_display_button_config_menu","memex_grouped_by_edit_route","memex_live_update_hovercard","memex_mwl_filter_field_delimiter","memex_roadmap_drag_style","mission_control_retry_on_401","mission_control_use_body_html","oauth_authorize_clickjacking_protection","open_agent_session_in_vscode_insiders","open_agent_session_in_vscode_stable","pr_comment_panel_footer","pr_sfv_new_diff_fetch","primer_react_css_has_selector_perf","projects_assignee_max_limit","prs_conversations_react","pull_request_files_accurate_size_estimates","pull_request_files_virtualization","pull_request_virtualization_preload_diffs","react_blob_overlay","react_quality_profiling","repo_agents_show_upgrade_slate","repos_allow_finder_filters_rollout","repos_finder_layout_route","repository_suggester_elastic_search","ruleset_deletion_confirmation","sample_network_conn_type","session_logs_ungroup_reasoning_text","site_calculator_actions_2025","site_features_copilot_universe","site_homepage_collaborate_video","spark_prompt_secret_scanning","spark_server_connection_status","suppress_automated_browser_vitals","suppress_non_representative_vitals","viewscreen_sandbox","webp_support","workbench_store_readonly"],"login":"serikkalijanaris-cyber","copilotApiOverrideUrl":"https://api.individual.githubcopilot.com"}</script>
<script crossorigin="anonymous" type="module" src="./def_files/wp-runtime-7e2653bfe7a6d16f.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/19762-203ba93c6a6f3066.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/49863-8861e351482cb073.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/64220-e17d13688e7db287.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/environment-2f7344d002077444.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/2966-25cb8e34b31306a4.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/96232-fb82336d69225835.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/41013-ac21ea90ed8590af.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/51210-185739338ae8119b.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/41121-3fac73a44ee7ce11.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/15814-aaebff5a797afefb.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/46740-84bdd4782a486b80.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/81751-750bd09cbdd426df.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/github-elements-aeed21930df5cfbb.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/element-registry-be60e37ce439c2d9.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/react-core-e91dca6e7d57c22c.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/react-lib-e74a1db7c21f7e74.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/7053-20b4a6914bbde21f.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/79039-9ce5da88e09eef89.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/61110-212553c409076913.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/2887-0e9a84f5dc250853.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/26533-6b8040883d16f6ae.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/62249-2895213a788d973c.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/16674-48fe19166d21f3ab.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/56093-fc82b6004a6fe178.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/28360-dc31a60141b9384f.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/65316-c849c86dc66fef72.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/22960-70bee7ef9ff9f7b2.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/51683-f6844a8acd415e3b.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/76545-cf3621a1f2f36d8d.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/behaviors-8e654050c72088f5.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/20475-e35ac743f34dd401.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/notifications-global-381343b9a90bbc8b.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/70447-7cc756a81ff96239.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/59572-89154da4565edea0.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/30476-733c3105e8b41a62.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/codespaces-a7598f1677c93e61.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/3064-ff9d0f819c141e10.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/89756-e7c55d48f60b581d.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/99291-ef227718ed886fe7.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/repositories-a71a3e8cf8c3cf6b.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/76181-4c0983f177d4dfc2.js.Без названия" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="./def_files/code-menu-71948db0153870ef.js.Без названия" defer="defer"></script>
  
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./def_files/primer-react.298ffe31d478a02c.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./def_files/notifications-subscriptions-menu.d0f37a7dc7f10fb3.module.css">


  



  
  
  
  

    
  


  


    


  
  

  
  

    







  

  




    

  

    

    

      

      

    
    
    

      
  
  


      
      


      


      
      
      

        


  <meta http-equiv="x-pjax-version" content="dd218054457474ed69be0d0e4cc3717afebf2dcf3fcf992a01ab80ee80352a78" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="21a43568025709b66240454fc92d4f09335a96863f8ab1c46b4a07f6a5b67102" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="d92a909a2d210296e2f536eb1c6d7d7e4892ca6f46eda5a0e6e7f518b66c2bb3" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="1bae9c7d08ea14e1ee9576041777790e900aa7d28044a68c6b15fb7dc65e3f07" data-turbo-track="reload">

  

      
  

  



      


    
  


  

  

  
  

  
  
  





  

  <link rel="stylesheet" type="text/css" href="./def_files/81758.57bb33287ab14521.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./def_files/38963.7bae12ca441bf5aa.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./def_files/7872.1af8557d38715a74.module.css" crossorigin="anonymous"><style data-styled="active" data-styled-version="5.3.11"></style><link rel="stylesheet" type="text/css" href="./def_files/96059.9c905a69b757e969.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./def_files/91539.2779c4a9de5108dd.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./def_files/98545.97b44ba3abd5dc65.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./def_files/19244.feb37fda150c0961.module.css" crossorigin="anonymous"><style id="ms-consent-banner-main-styles">.w8hcgFksdo30C8w-bygqu{color:#000}.ydkKdaztSS0AeHWIeIHsQ a{color:#0067B8}.erL690_8JwUW-R4bJRcfl{background-color:#EBEBEB;border:none;color:#000}.erL690_8JwUW-R4bJRcfl:enabled:hover{color:#000;background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}.erL690_8JwUW-R4bJRcfl:enabled:focus{background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}.erL690_8JwUW-R4bJRcfl:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2);border:none}._1zNQOqxpBFSokeCLGi_hGr{border:none;background-color:#0067B8;color:#fff}._1zNQOqxpBFSokeCLGi_hGr:enabled:hover{color:#fff;background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}._1zNQOqxpBFSokeCLGi_hGr:enabled:focus{background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}._1zNQOqxpBFSokeCLGi_hGr:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,120,215,0.2);border:none}._23tra1HsiiP6cT-Cka-ycB{position:relative;display:flex;z-index:9999;width:100%;background-color:#F2F2F2;justify-content:space-between;text-align:left}div[dir="rtl"]._23tra1HsiiP6cT-Cka-ycB{text-align:right}._1Upc2NjY8AlDn177YoVj0y{margin:0;padding-left:5%;padding-top:8px;padding-bottom:8px}div[dir="rtl"] ._1Upc2NjY8AlDn177YoVj0y{margin:0;padding:8px 5% 8px 0;float:none}._23tra1HsiiP6cT-Cka-ycB svg{fill:none;max-width:none;max-height:none}._1V_hlU-7jdtPiooHMu89BB{display:table-cell;padding:12px;width:24px;height:24px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:24px;line-height:0}.f6QKJD7fhSbnJLarTL-W-{display:table-cell;vertical-align:middle;padding:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:16px}.f6QKJD7fhSbnJLarTL-W- a{text-decoration:underline}._2j0fmugLb1FgYz6KPuB91w{display:inline-block;margin-left:5%;margin-right:5%;min-width:40%;min-width:calc((150px + 3 * 4px) * 2 + 150px);min-width:-webkit-fit-content;min-width:-moz-fit-content;min-width:fit-content;align-self:center;position:relative}._1XuCi2WhiqeWRUVp3pnFG3{margin:4px;padding:5px;min-width:150px;min-height:36px;vertical-align:top;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._1XuCi2WhiqeWRUVp3pnFG3:focus{box-sizing:border-box}._1XuCi2WhiqeWRUVp3pnFG3:disabled{cursor:not-allowed}._2bvsb3ubApyZ0UGoQA9O9T{display:block;position:fixed;z-index:10000;top:0;left:0;width:100%;height:100%;background-color:rgba(255,255,255,0.6);overflow:auto;text-align:left}div[dir="rtl"]._2bvsb3ubApyZ0UGoQA9O9T{text-align:right}div[dir="rtl"] ._2bvsb3ubApyZ0UGoQA9O9T{left:auto;right:0}.AFsJE948muYyzCMktdzuk{position:relative;top:8%;margin-bottom:40px;margin-left:auto;margin-right:auto;box-sizing:border-box;width:640px;background-color:#fff;border:1px solid #0067B8}._3kWyBRbW_dgnMiEyx06Fu4{float:right;z-index:1;margin:2px;padding:12px;border:none;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:13px;display:flex;align-items:center;text-align:center;color:#666;background-color:#fff}div[dir="rtl"] ._3kWyBRbW_dgnMiEyx06Fu4{margin:2px;padding:12px;float:left}.uCYvKvHXrhjNgflv1VqdD{position:static;margin-top:36px;margin-left:36px;margin-right:36px}._17pX1m9O_W--iZbDt3Ta5r{margin-top:0;margin-bottom:12px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:20px;line-height:24px;text-transform:none}._1kBkHQ1V1wu3kl-YcLgUr6{height:446px;overflow:auto}._20_nXDf6uFs9Q6wxRXG-I-{margin-top:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._20_nXDf6uFs9Q6wxRXG-I- a{text-decoration:underline}dl._2a0NH_GDQEQe5Ynfo7suVH{margin-top:36px;margin-bottom:0;padding:0;list-style:none;text-transform:none}dt._3j_LCPv7fyXv3A8FIXVwZ4{margin-top:20px;float:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;list-style:none}.k-vxTGFbdq1aOZB2HHpjh{margin:0;padding:0;border:none}._2Bucyy75c_ogoU1g-liB5R{margin:0;padding:0;border-bottom:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;text-transform:none}._63gwfzV8dclrsl2cfd90r{display:inline-block;margin-top:0;margin-bottom:13px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._1l8wM_4mRYGz3Iu7l3BZR7{display:block}._2UE03QS02aZGkslegN_F-i{display:inline-block;position:relative;left:5px;margin-bottom:13px;margin-right:34px;padding:3px}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{margin:0 0 13px 34px;padding:3px;float:none}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{left:auto;right:5px}._23tra1HsiiP6cT-Cka-ycB *::before,._2bvsb3ubApyZ0UGoQA9O9T *::before,._23tra1HsiiP6cT-Cka-ycB *::after,._2bvsb3ubApyZ0UGoQA9O9T *::after{box-sizing:inherit}._1HSFn0HzGo6w4ADApV8-c4{outline:2px solid rgba(0,0,0,0.8)}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2{display:inline-block;position:relative;margin-top:0;margin-left:0;margin-right:0;height:0;width:0;border-radius:0;cursor:pointer;outline:none;box-sizing:border-box;-webkit-appearance:none;-moz-appearance:none;appearance:none}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{display:block;position:absolute;top:5px;left:3px;height:19px;width:19px;content:"";border-radius:50%;border:1px solid #000;background-color:#fff}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{left:auto;right:3px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:rgba(0,0,0,0.8)}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label{cursor:not-allowed}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label::before{border:1px solid rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2)}._3RJzeL3l9Rl_lAQEm6VwdX{display:block;position:static;float:right;margin-top:0;margin-bottom:0;margin-left:19px;margin-right:0;padding-top:0;padding-bottom:0;padding-left:8px;padding-right:0;width:80%;width:calc(100% - 19px);font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-transform:none;cursor:pointer;box-sizing:border-box}div[dir="rtl"] ._3RJzeL3l9Rl_lAQEm6VwdX{margin:0 19px 0 0;padding:0 8px 0 0;float:left}.nohp3sIG12ZBhzcMnPala{margin-top:20px;margin-bottom:48px}._2uhaEsmeotZ3P-M0AXo2kF{padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._2uhaEsmeotZ3P-M0AXo2kF:focus{box-sizing:border-box}._2uhaEsmeotZ3P-M0AXo2kF:disabled{cursor:not-allowed}._3tOu1FJ59c_xz_PmI1lKV5{float:right;padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._3tOu1FJ59c_xz_PmI1lKV5:focus{box-sizing:border-box}._3tOu1FJ59c_xz_PmI1lKV5:disabled{cursor:not-allowed}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0;padding:0;float:left}@media only screen and (max-width: 768px){._2j0fmugLb1FgYz6KPuB91w,._1Upc2NjY8AlDn177YoVj0y{padding-top:8px;padding-bottom:12px;padding-left:3.75%;padding-right:3.75%;margin:0;width:92.5%}._23tra1HsiiP6cT-Cka-ycB{display:block}._1XuCi2WhiqeWRUVp3pnFG3{margin-bottom:8px;margin-left:0;margin-right:0;width:100%}._2bvsb3ubApyZ0UGoQA9O9T{overflow:hidden}.AFsJE948muYyzCMktdzuk{top:1.8%;width:93.33%;height:96.4%;overflow:hidden}.uCYvKvHXrhjNgflv1VqdD{margin-top:24px;margin-left:24px;margin-right:24px;height:100%}._1kBkHQ1V1wu3kl-YcLgUr6{height:62%;height:calc(100% - 188px);min-height:50%}._2uhaEsmeotZ3P-M0AXo2kF{width:100%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:12px;margin-left:0;width:100%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 12px 0;padding:0;float:none}}@media only screen and (max-width: 768px) and (orientation: landscape), only screen and (max-height: 260px), only screen and (max-width: 340px){.AFsJE948muYyzCMktdzuk{overflow:auto}}@media only screen and (max-height: 260px), only screen and (max-width: 340px){._1XuCi2WhiqeWRUVp3pnFG3{min-width:0}._3kWyBRbW_dgnMiEyx06Fu4{padding:3%}.uCYvKvHXrhjNgflv1VqdD{margin-top:3%;margin-left:3%;margin-right:3%}._17pX1m9O_W--iZbDt3Ta5r{margin-bottom:3%}._1kBkHQ1V1wu3kl-YcLgUr6{height:calc(79% - 64px)}.nohp3sIG12ZBhzcMnPala{margin-top:5%;margin-bottom:10%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:3%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 3% 0;padding:0;float:none}}
</style><style type="text/css" id="ms-consent-banner-theme-styles">._23tra1HsiiP6cT-Cka-ycB {
            background-color: #24292f !important;
        }.w8hcgFksdo30C8w-bygqu {
            color: #ffffff !important;
        }.ydkKdaztSS0AeHWIeIHsQ a {
            color: #d8b9ff !important;
        }._2bvsb3ubApyZ0UGoQA9O9T {
            background-color: rgba(23, 23, 23, 0.8) !important;
        }.AFsJE948muYyzCMktdzuk {
            background-color: #24292f !important;
            border: 1px solid #d8b9ff !important;
        }._3kWyBRbW_dgnMiEyx06Fu4 {
            color: #d8b9ff !important;
            background-color: #24292f !important;
        }._1zNQOqxpBFSokeCLGi_hGr {
            border: 1px solid #ffffff !important;
            background-color: #ffffff !important;
            color: #1f2328 !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:hover {
            color: #1f2328 !important;
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 1px solid transparent !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:focus {
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 2px solid #ffffff !important;
        }._1zNQOqxpBFSokeCLGi_hGr:disabled {
            opacity: 0.5 !important;
            color: #1f2328 !important;
            background-color: #ffffff !important;
            border: 1px solid transparent !important;
        }.erL690_8JwUW-R4bJRcfl {
            border: 1px solid #eaeef2 !important;
            background-color: #32383f !important;
            color: #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:hover {
            color: #ffffff !important;
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 1px solid #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:focus {
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 2px solid #6e7781 !important;
        }.erL690_8JwUW-R4bJRcfl:disabled {
            opacity: 0.5 !important;
            color: #ffffff !important;
            background-color: #424a53 !important;
            border: 1px solid #6e7781 !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label::before {
            border: 1px solid #d8b9ff !important;
            background-color: #24292f !important;
        }._1HSFn0HzGo6w4ADApV8-c4 {
            outline: 2px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked + label::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::after {
            background-color: #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled + label::before {
            border: 1px solid rgba(227, 227, 227, 0.2) !important;
            background-color: rgba(227, 227, 227, 0.2) !important;
        }</style><link rel="stylesheet" type="text/css" href="./def_files/26330.f943e417bdb5f4c2.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./def_files/68269.165e2f3b5e4cdec1.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./def_files/74861.a9ccec65608a5b7f.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./def_files/10073.ffc363935a56bcf8.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./def_files/53957.6c9ad28605ea1eaf.module.css" crossorigin="anonymous"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./def_files/49396.d3c6b22f072bca01.module.css"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./def_files/98562.a04e1a16d5bb1d0f.module.css"><script type="module" src="./def_files/primer-react-89c49a44d226f6bb.js.Без названия"></script><script type="module" src="./def_files/octicons-react-39f7eb9c9327cc85.js.Без названия"></script><script type="module" src="./def_files/59660-3d5114bc5964e225.js.Без названия"></script><script type="module" src="./def_files/73694-9ce8f07e75948540.js.Без названия"></script><script type="module" src="./def_files/68751-4d3d1aac1f81a213.js.Без названия"></script><script type="module" src="./def_files/42688-0b9cda7be58af629.js.Без названия"></script><script type="module" src="./def_files/13835-e2fda693a3199c15.js.Без названия"></script><script type="module" src="./def_files/7463-2a94d884e276b7f9.js.Без названия"></script><script type="module" src="./def_files/32769-e856688499efb8d1.js.Без названия"></script><script type="module" src="./def_files/437-ed451d0ef5202580.js.Без названия"></script><script type="module" src="./def_files/77499-85ec5820c24f9322.js.Без названия"></script><script type="module" src="./def_files/20992-fe53d17e65ffb933.js.Без названия"></script><script type="module" src="./def_files/99280-1107845662773be8.js.Без названия"></script><script type="module" src="./def_files/16111-364cf74b4896f28d.js.Без названия"></script><script type="module" src="./def_files/62095-57aaf0e9da8f599e.js.Без названия"></script><script type="module" src="./def_files/38728-8f994d5a3eed759f.js.Без названия"></script><script type="module" src="./def_files/99602-57e3e2867064ab92.js.Без названия"></script><script type="module" src="./def_files/71365-07760cdad88d536f.js.Без названия"></script><script type="module" src="./def_files/11152-ab31b20bfdc6794f.js.Без названия"></script><script type="module" src="./def_files/61300-5b757d8ceaadae40.js.Без названия"></script><script type="module" src="./def_files/41954-a5d8ec32c45aaef5.js.Без названия"></script><script type="module" src="./def_files/65439-3097f4fb22aad2d9.js.Без названия"></script><script type="module" src="./def_files/72807-c884a8278526ac5a.js.Без названия"></script><script type="module" src="./def_files/78563-3e58802bd3476e08.js.Без названия"></script><script type="module" src="./def_files/16073-64479e3f710ca2cd.js.Без названия"></script><script type="module" src="./def_files/97274-09f2551718e5bab8.js.Без названия"></script><script type="module" src="./def_files/16251-d2a9c9fd1a41b965.js.Без названия"></script><script type="module" src="./def_files/43142-60af73dbb047bb6a.js.Без названия"></script><script type="module" src="./def_files/49396-b032d9d2e04efa8e.js.Без названия"></script><script type="module" src="./def_files/80352-37f58cb7111a3a54.js.Без названия"></script><script type="module" src="./def_files/11268-4a7f14af6ade18ca.js.Без названия"></script><script type="module" src="./def_files/73494-540182b632e1b952.js.Без названия"></script><script type="module" src="./def_files/98562-6131478b30349fe7.js.Без названия"></script><script type="module" src="./def_files/react-code-view-86d25d2c27f536ef.js.Без названия"></script><style data-styled="true" data-styled-version="5.3.11" data-react-root-id="f5766d1c-31c8-4641-8a14-afc73b8d80b9">.jmjlbk{width:100%;}/*!sc*/
@media screen and (min-width:544px){.jmjlbk{width:100%;}}/*!sc*/
@media screen and (min-width:768px){.jmjlbk{width:auto;}}/*!sc*/
.fvNWEZ{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;width:100%;margin-bottom:16px;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;}/*!sc*/
.cybVuK{margin-left:auto;margin-right:auto;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;padding-bottom:40px;max-width:100%;margin-top:0;}/*!sc*/
.gSjuRy{display:inherit;}/*!sc*/
.jyTWxL{margin-left:16px;margin-right:16px;}/*!sc*/
.kntYzq{top:0px;z-index:0;background:var(--bgColor-default,var(--color-canvas-default));position:-webkit-sticky;position:sticky;}/*!sc*/
.jiqOwO{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;background-color:var(--bgColor-muted,var(--color-canvas-subtle,#161b22));border-bottom:none;overflow:hidden;}/*!sc*/
.iNRqcN{display:none;min-width:0;padding-top:8px;padding-bottom:8px;}/*!sc*/
.jAIDYE{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;gap:16px;}/*!sc*/
.vdPNv{position:fixed;top:0;right:0;height:100%;width:15px;-webkit-transition:-webkit-transform 0.3s;-webkit-transition:transform 0.3s;transition:transform 0.3s;z-index:1;}/*!sc*/
.vdPNv:hover{-webkit-transform:scaleX(1.5);-ms-transform:scaleX(1.5);transform:scaleX(1.5);}/*!sc*/
data-styled.g1[id="Box-sc-62in7e-0"]{content:"jmjlbk,fvNWEZ,cybVuK,gSjuRy,jyTWxL,kntYzq,jiqOwO,iNRqcN,jAIDYE,vdPNv,"}/*!sc*/
.dWfbpP{font-size:16px;margin-left:8px;}/*!sc*/
data-styled.g21[id="Heading-sc-1vc165i-0"]{content:"dWfbpP,"}/*!sc*/
</style><link rel="dns-prefetch" href="https://github.githubassets.com/"><link rel="dns-prefetch" href="https://avatars.githubusercontent.com/"><link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com/"><link rel="dns-prefetch" href="https://user-images.githubusercontent.com/"><link rel="preconnect" href="https://github.githubassets.com/" crossorigin=""><link rel="preconnect" href="https://avatars.githubusercontent.com/"><title>pp2_v_kha/practise3/classes/class_defenition.py at main · khavadim1-cyber/pp2_v_kha</title><meta name="fetch-nonce" content="v2:9d1a1c28-e451-6476-3dc6-ca94ab92f7d8"><meta name="current-catalog-service-hash" content="f3abb0cc802f3d7b95fc8762b94bdcb13bf39634c40c357301c4aa1d67a256fb"><link rel="assets" href="https://github.githubassets.com/"><meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I"><meta name="octolytics-url" content="https://collector.github.com/github/collect"><meta name="octolytics-actor-id" content="257359913"><meta name="octolytics-actor-login" content="serikkalijanaris-cyber"><meta name="octolytics-actor-hash" content="e97a57ea5c0942635dc992b73820fb6fdb1433c894d5eddb052ed80034efe650"><meta name="user-login" content="serikkalijanaris-cyber"><link rel="sudo-modal" href="https://github.com/sessions/sudo_modal"><meta name="viewport" content="width=device-width"><meta name="description" content="Contribute to khavadim1-cyber/pp2_v_kha development by creating an account on GitHub."><link rel="search" type="application/opensearchdescription+xml" href="https://github.com/opensearch.xml" title="GitHub"><link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub"><meta property="fb:app_id" content="1401488693436528"><meta name="apple-itunes-app" content="app-id=1477376905, app-argument=https://github.com/khavadim1-cyber/pp2_v_kha"><meta name="twitter:image" content="https://opengraph.githubassets.com/c35ab58e2ae0c1c0705ef73260112e328e8ab5f6968c974b686b45ca4245cb1e/khavadim1-cyber/pp2_v_kha"><meta name="twitter:site" content="@github"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="khavadim1-cyber/pp2_v_kha"><meta name="twitter:description" content="Contribute to khavadim1-cyber/pp2_v_kha development by creating an account on GitHub."><meta property="og:image" content="https://opengraph.githubassets.com/c35ab58e2ae0c1c0705ef73260112e328e8ab5f6968c974b686b45ca4245cb1e/khavadim1-cyber/pp2_v_kha"><meta property="og:image:alt" content="Contribute to khavadim1-cyber/pp2_v_kha development by creating an account on GitHub."><meta property="og:image:width" content="1200"><meta property="og:image:height" content="600"><meta property="og:site_name" content="GitHub"><meta property="og:type" content="object"><meta property="og:title" content="khavadim1-cyber/pp2_v_kha"><meta property="og:url" content="https://github.com/khavadim1-cyber/pp2_v_kha"><meta property="og:description" content="Contribute to khavadim1-cyber/pp2_v_kha development by creating an account on GitHub."><link rel="shared-web-socket" href="wss://alive.github.com/_sockets/u/257359913/ws?session=eyJ2IjoiVjMiLCJ1IjoyNTczNTk5MTMsInMiOjE5NDc2MjU2NDgsImMiOjU4MjM3ODk0LCJ0IjoxNzcxMjcxMjEzfQ==--515aad385d5517d2d7a1fd192e06510930d7d200ef8c0f4d6ea87cdd9d62c62f" data-refresh-url="/_alive" data-session-id="d8a13006628be665fb216741a786dd35d1579f1df9ae8f32baf8d97043cf037f"><link rel="shared-web-socket-src" href="https://github.com/assets-cdn/worker/socket-worker-9c03177cabef2321.js"><meta name="hostname" content="github.com"><meta name="keyboard-shortcuts-preference" content="all"><meta name="hovercards-preference" content="true"><meta name="announcement-preference-hovercard" content="true"><meta name="expected-hostname" content="github.com"><meta data-hydrostats="publish"><meta name="go-import" content="github.com/khavadim1-cyber/pp2_v_kha git https://github.com/khavadim1-cyber/pp2_v_kha.git"><meta name="octolytics-dimension-user_id" content="230659265"><meta name="octolytics-dimension-user_login" content="khavadim1-cyber"><meta name="octolytics-dimension-repository_id" content="1138022152"><meta name="octolytics-dimension-repository_nwo" content="khavadim1-cyber/pp2_v_kha"><meta name="octolytics-dimension-repository_public" content="true"><meta name="octolytics-dimension-repository_is_fork" content="false"><meta name="octolytics-dimension-repository_network_root_id" content="1138022152"><meta name="octolytics-dimension-repository_network_root_nwo" content="khavadim1-cyber/pp2_v_kha"><meta name="turbo-body-classes" content="logged-in env-production page-responsive"><meta name="disable-turbo" content="false"><meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats"><meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors"><meta name="release" content="5a52920e968b8ae3bc55e6099e37b07d0515300e"><meta name="ui-target" content="full"><link rel="mask-icon" href="https://github.githubassets.com/assets/pinned-octocat-093da3e6fa40.svg" color="#000000"><link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon-dark.png"><link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon-dark.svg" data-base-href="https://github.githubassets.com/favicons/favicon"><meta name="theme-color" content="#1e2327"><meta name="color-scheme" content="light dark"><link rel="manifest" href="https://github.com/manifest.json" crossorigin="use-credentials"><meta name="route-pattern" content="/:user_id/:repository/tree/*name(/*path)" data-turbo-transient=""><meta name="route-controller" content="files" data-turbo-transient=""><meta name="route-action" content="disambiguate" data-turbo-transient=""><meta name="selected-link" value="repo_source" data-turbo-transient=""><meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/files/disambiguate" data-turbo-transient=""><meta name="request-id" content="DC1E:164963:12AC67A:E3E490:69937430" data-turbo-transient=""><meta name="html-safe-nonce" content="9dea5d3dfef74b76f12c66d2de74e3d7a0247a2479c088109d2521b55687b538" data-turbo-transient=""><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS9raGF2YWRpbTEtY3liZXIvcHAyX3Zfa2hhL2Jsb2IvbWFpbi9wcmFjdGlzZTMvY2xhc3Nlcy9jbGFzc19kZWZlbml0aW9uLnB5IiwicmVxdWVzdF9pZCI6IkRDMUU6MTY0OTYzOjEyQUM2N0E6RTNFNDkwOjY5OTM3NDMwIiwidmlzaXRvcl9pZCI6Ijc5NDAwNDE3ODkxNjIxNTExNjciLCJyZWdpb25fZWRnZSI6ImZyYSIsInJlZ2lvbl9yZW5kZXIiOiJpYWQifQ==" data-turbo-transient=""><meta name="visitor-hmac" content="d15edca66296035e7d9bb0db306d57336a8c2b22b7c1eb53b7d439973c35eb7e" data-turbo-transient=""><meta name="github-keyboard-shortcuts" content="repository,source-code,file-tree,copilot" data-turbo-transient=""><meta name="hovercard-subject-tag" content="repository:1138022152" data-turbo-transient=""><meta name="turbo-cache-control" content="no-preview" data-turbo-transient=""><meta name="turbo-cache-control" content="no-cache" data-turbo-transient=""></head>

  <body class="logged-in env-production page-responsive" style="overflow-wrap: break-word; --dialog-scrollgutter: 15px;" data-dialog-scroll-optimized="">
    <div data-turbo-body="" class="logged-in env-production page-responsive" style="word-wrap: break-word;">
      <div id="__primerPortalRoot__" role="region" style="z-index: 1000; position: absolute; width: 100%;" data-turbo-permanent=""></div>
      

    <div class="position-relative header-wrapper js-header-wrapper ">
      <a href="https://github.com/khavadim1-cyber/pp2_v_kha/blob/main/practise3/classes/class_defenition.py#start-of-content" data-skip-target-assigned="false" class="p-3 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>

      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      
      <link crossorigin="anonymous" media="all" rel="stylesheet" href="./def_files/primer-react.298ffe31d478a02c.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./def_files/keyboard-shortcuts-dialog.6268703e736b56bb.module.css">

<react-partial partial-name="keyboard-shortcuts-dialog" data-ssr="false" data-attempted-ssr="false" data-react-profiling="true" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"docsUrl":"https://docs.github.com/get-started/accessibility/keyboard-shortcuts"}}</script>
  <div data-target="react-partial.reactRoot"><div class="d-none"></div><script type="application/json" id="__PRIMER_DATA__r_0___">{"resolvedServerColorMode":"night"}</script></div>
</react-partial>





      

          

                  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./def_files/primer-react.298ffe31d478a02c.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./def_files/global-nav-bar.d49721c1a61525af.module.css">

<react-partial partial-name="global-nav-bar" data-ssr="true" data-attempted-ssr="true" data-react-profiling="true" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"contextRegion":{"crumbs":[{"crumb_type":"user","label":"khavadim1-cyber","is_root":false,"href":"/khavadim1-cyber"},{"crumb_type":"repository","label":"pp2_v_kha","is_root":false,"href":"/khavadim1-cyber/pp2_v_kha"}],"localNavigation":[{"id":"code","icon":"code","label":"Code","href":"/khavadim1-cyber/pp2_v_kha","selectedLinks":["repo_source","repo_downloads","repo_commits","repo_releases","repo_tags","repo_branches","repo_packages","repo_deployments","repo_attestations"],"popoverTarget":false,"hotkey":"g c","reactNav":{"appTarget":"code-view","anchor":"code-view-repo-link"},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"issues","icon":"issue-opened","label":"Issues","href":"/khavadim1-cyber/pp2_v_kha/issues","selectedLinks":["repo_issues","repo_labels","repo_milestones"],"count":0,"popoverTarget":false,"hotkey":"g i","reactNav":{"appTarget":"issues-react","anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"pull-requests","icon":"git-pull-request","label":"Pull requests","href":"/khavadim1-cyber/pp2_v_kha/pulls","selectedLinks":["repo_pulls","checks"],"count":0,"popoverTarget":false,"hotkey":"g p","reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"agents","icon":"agent","label":"Agents","href":"/khavadim1-cyber/pp2_v_kha/agents?author=serikkalijanaris-cyber","selectedLinks":["repo_agents","repo_agents_task"],"popoverTarget":false,"hotkey":"g e","reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"actions","icon":"play","label":"Actions","href":"/khavadim1-cyber/pp2_v_kha/actions","selectedLinks":["repo_actions"],"popoverTarget":false,"hotkey":"g a","reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"projects","icon":"table","label":"Projects","href":"/khavadim1-cyber/pp2_v_kha/projects","selectedLinks":["repo_projects","new_repo_project","repo_project"],"count":0,"popoverTarget":false,"hotkey":"g b","reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"security","icon":"shield","label":"Security","href":"/khavadim1-cyber/pp2_v_kha/security","selectedLinks":["security","overview","alerts","policy","token_scanning","code_scanning"],"count":0,"popoverTarget":false,"hotkey":"g s","reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}},{"id":"insights","icon":"graph","label":"Insights","href":"/khavadim1-cyber/pp2_v_kha/pulse","selectedLinks":["repo_graphs","repo_contributors","dependency_graph","dependabot_updates","pulse","people","community"],"popoverTarget":false,"reactNav":{"appTarget":null,"anchor":null},"turboNav":{"frame":"repo-content-turbo-frame"}}],"localNavigationUpdateChannel":"eyJjIjoicmVwbzoxMTM4MDIyMTUyOnVzZXI6MjU3MzU5OTEzOnNldHRpbmdzIiwidCI6MTc3MTI3MTIxM30=--3edd0ac40928e1be9d3469d974f691b38514e6d9bf86179e95dd89db4e3324a9","selectedLink":"repo_source"},"navMenu":{"home":{"href":"https://github.com/dashboard","hotkey":"g d"},"feed":{"show":false,"href":"https://github.com/feed"},"issues":{"href":"https://github.com/issues","hotkey":"g i"},"pulls":{"href":"https://github.com/pulls","hotkey":"g p"},"contributedRepos":{"show":true,"href":"https://github.com/repos","hotkey":null},"projects":{"href":"https://github.com/projects"},"discussions":{"show":true,"href":"https://github.com/discussions"},"codespaces":{"show":true,"href":"https://github.com/codespaces"},"copilot":{"show":true,"href":"/copilot"},"spark":{"show":false,"href":null},"marketplace":{"show":true,"href":"https://github.com/marketplace"},"mcp":{"show":true,"href":"https://github.com/mcp"},"explore":{"show":true,"href":"https://github.com/explore"},"richContent":{"show":true,"contentUrl":"/_side-panels/global.json","repositoriesSearchUrl":"/_side-panel-items/global/repositories.json"}},"accountSwitchDialog":{"show":false},"globalTransactionalMessage":null,"userMenu":{"owner":{"login":"serikkalijanaris-cyber","name":null,"avatarUrl":"https://avatars.githubusercontent.com/u/257359913?v=4"},"drawerId":"global-user-nav-drawer","lazyLoadItemDataFetchUrl":"/_side-panels/user.json","canAddAccount":true,"addAccountPath":"/login?add_account=1\u0026return_to=https%3A%2F%2Fgithub.com%2Fkhavadim1-cyber%2Fpp2_v_kha","switchAccountPath":"/switch_account","loginAccountPath":"/login?add_account=1","projectsPath":"/serikkalijanaris-cyber?tab=projects","gistsUrl":"https://gist.github.com/mine","docsUrl":"https://docs.github.com","yourEnterpriseUrl":null,"enterpriseSettingsUrl":null,"supportUrl":"https://support.github.com","showAccountSwitcher":true,"showCopilot":true,"showEnterprises":true,"showEnterprise":false,"showGists":true,"showOrganizations":true,"showSponsors":true,"showUpgrade":true,"showFeaturesPreviews":true,"showEnterpriseSettings":false},"createMenu":{"showCreateRepo":true,"showImportRepo":true,"showCodespaces":true,"showSpark":false,"showCodingAgent":false,"showGist":true,"showCreateOrg":true,"showCreateProject":false,"showCreateLegacyProject":false,"showCreateIssue":true,"createProjectUrl":"/serikkalijanaris-cyber?tab=projects","org":null,"owner":"khavadim1-cyber","repo":"pp2_v_kha"},"headerLogo":{"href":"https://github.com/","hotkey":"g d","aria-label":"Homepage "},"notifications":{"hotkey":"g n","indicatorMode":"none","websocketChannel":"eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MjU3MzU5OTEzIiwidCI6MTc3MTI3MTIxM30=--d8e1c2f198e620220c378f3f6a0248aa8a63eb6258ed10969bf77065c0d954ea","fetchIndicatorSrc":"/notifications/indicator","fetchIndicatorEnabled":true},"issues":{"href":"https://github.com/issues","hotkey":"g i"},"pulls":{"href":"https://github.com/pulls","hotkey":"g p"},"contributedRepos":{"show":true,"href":"https://github.com/repos","hotkey":null},"copilot":{"show":true,"showCopilotTitle":false,"showAgentsButton":false,"copilotChatUrl":"/github-copilot/chat?skip_anchor=true","copilotApiUrl":"https://api.individual.githubcopilot.com","agentsPanel":null},"search":{"show":true,"searchHotkey":"s,/","showCommandPalette":false,"commandPaletteHotkey":null,"isSearchPage":false,"isJumpToSearch":false,"fragmentsPath":"/_global-navigation/fragments","fragmentsParams":null},"enterpriseBanner":{"show":false}}}</script>
  <div data-target="react-partial.reactRoot"><link rel="preload" as="image" href="./def_files/257359913"><header role="banner" aria-label="Global Navigation Menu" class="GlobalNav styles-module__appHeader__YzYWk prc-Stack-Stack-UQ9k6" data-gap="none" data-direction="vertical" data-align="stretch" data-wrap="nowrap" data-justify="start" data-padding="none"><div class="prc-Stack-Stack-UQ9k6" data-direction="horizontal" data-align="center" data-wrap="nowrap" data-justify="center" data-padding="none"><div data-testid="top-nav-left" class="styles-module__left__Fylw7 styles-module__withLocalNavigation__rjTJ_ prc-Stack-Stack-UQ9k6" data-gap="condensed" data-direction="horizontal" data-align="stretch" data-wrap="nowrap" data-justify="start" data-padding="normal"><div data-loading-wrapper="true"><button data-component="IconButton" type="button" aria-haspopup="dialog" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_apb_"><svg aria-hidden="true" focusable="false" class="octicon octicon-three-bars" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1 2.75A.75.75 0 0 1 1.75 2h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 2.75Zm0 5A.75.75 0 0 1 1.75 7h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 7.75ZM1.75 12h12.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5Z"></path></svg></button></div><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id="_R_apb_" popover="auto">Open menu</span><div class="d-none"><li data-has-description="false" class="prc-ActionList-ActionListItem-So4vC"><a class="prc-ActionList-ActionListContent-KBb8- prc-Link-Link-9ZwDx" tabindex="0" aria-labelledby="_r_1g_--label  " id="_r_1g_" data-size="medium" href="https://github.com/dashboard" data-testid="side-nav-menu-item-HOME" style="--subitem-depth: 0;"><span class="prc-ActionList-Spacer-4tR2m"></span><span class="prc-ActionList-LeadingVisual-NBr28 prc-ActionList-VisualWrap-bdCsS"><svg aria-hidden="true" focusable="false" class="octicon octicon-home" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M6.906.664a1.749 1.749 0 0 1 2.187 0l5.25 4.2c.415.332.657.835.657 1.367v7.019A1.75 1.75 0 0 1 13.25 15h-3.5a.75.75 0 0 1-.75-.75V9H7v5.25a.75.75 0 0 1-.75.75h-3.5A1.75 1.75 0 0 1 1 13.25V6.23c0-.531.242-1.034.657-1.366l5.25-4.2Zm1.25 1.171a.25.25 0 0 0-.312 0l-5.25 4.2a.25.25 0 0 0-.094.196v7.019c0 .138.112.25.25.25H5.5V8.25a.75.75 0 0 1 .75-.75h3.5a.75.75 0 0 1 .75.75v5.25h2.75a.25.25 0 0 0 .25-.25V6.23a.25.25 0 0 0-.094-.195Z"></path></svg></span><span class="prc-ActionList-ActionListSubContent-gKsFp" data-component="ActionList.Item--DividerContainer"><span id="_r_1g_--label" class="prc-ActionList-ItemLabel-81ohH">Home</span></span></a></li><li data-has-description="false" class="prc-ActionList-ActionListItem-So4vC"><a class="prc-ActionList-ActionListContent-KBb8- prc-Link-Link-9ZwDx" tabindex="0" aria-labelledby="_r_1h_--label  " id="_r_1h_" data-size="medium" href="https://github.com/issues" data-testid="side-nav-menu-item-ISSUES" style="--subitem-depth: 0;"><span class="prc-ActionList-Spacer-4tR2m"></span><span class="prc-ActionList-LeadingVisual-NBr28 prc-ActionList-VisualWrap-bdCsS"><svg aria-hidden="true" focusable="false" class="octicon octicon-issue-opened" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path></svg></span><span class="prc-ActionList-ActionListSubContent-gKsFp" data-component="ActionList.Item--DividerContainer"><span id="_r_1h_--label" class="prc-ActionList-ItemLabel-81ohH">Issues</span></span></a></li><li data-has-description="false" class="prc-ActionList-ActionListItem-So4vC"><a class="prc-ActionList-ActionListContent-KBb8- prc-Link-Link-9ZwDx" tabindex="0" aria-labelledby="_r_1i_--label  " id="_r_1i_" data-size="medium" href="https://github.com/pulls" data-testid="side-nav-menu-item-PULL_REQUESTS" style="--subitem-depth: 0;"><span class="prc-ActionList-Spacer-4tR2m"></span><span class="prc-ActionList-LeadingVisual-NBr28 prc-ActionList-VisualWrap-bdCsS"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-pull-request" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path></svg></span><span class="prc-ActionList-ActionListSubContent-gKsFp" data-component="ActionList.Item--DividerContainer"><span id="_r_1i_--label" class="prc-ActionList-ItemLabel-81ohH">Pull requests</span></span></a></li></div><a data-component="IconButton" type="button" href="https://github.com/" data-hotkey="g d" hotkey="g d" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderHome__nkA_U prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_4pb_"><svg aria-hidden="true" focusable="false" class="octicon octicon-mark-github" viewBox="0 0 24 24" width="32" height="32" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M12 1C5.923 1 1 5.923 1 12c0 4.867 3.149 8.979 7.521 10.436.55.096.756-.233.756-.522 0-.262-.013-1.128-.013-2.049-2.764.509-3.479-.674-3.699-1.292-.124-.317-.66-1.293-1.127-1.554-.385-.207-.936-.715-.014-.729.866-.014 1.485.797 1.691 1.128.99 1.663 2.571 1.196 3.204.907.096-.715.385-1.196.701-1.471-2.448-.275-5.005-1.224-5.005-5.432 0-1.196.426-2.186 1.128-2.956-.111-.275-.496-1.402.11-2.915 0 0 .921-.288 3.024 1.128a10.193 10.193 0 0 1 2.75-.371c.936 0 1.871.123 2.75.371 2.104-1.43 3.025-1.128 3.025-1.128.605 1.513.221 2.64.111 2.915.701.77 1.127 1.747 1.127 2.956 0 4.222-2.571 5.157-5.019 5.432.399.344.743 1.004.743 2.035 0 1.471-.014 2.654-.014 3.025 0 .289.206.632.756.522C19.851 20.979 23 16.854 23 12c0-6.077-4.922-11-11-11Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" popover="auto"><span id="_R_4pb_">Homepage <span class="prc-src-InternalVisuallyHidden-2YaI6">(<!-- -->g then d<!-- -->)</span></span><span class="prc-TooltipV2-KeybindingHintContainer-Ymj-3 prc-TooltipV2-HasTextBefore-fdOXj" aria-hidden="true"><kbd class="prc-KeybindingHint-KeybindingHint-qpYIs prc-Text-Text-9mHv3" data-testid="keybinding-hint"><span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">g</span><span aria-hidden="true">G</span></span><span class="prc-src-InternalVisuallyHidden-2YaI6">then</span> <span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">d</span><span aria-hidden="true">D</span></span></kbd></span></span></div><div data-testid="top-nav-center" class="styles-module__center__R3QRv styles-module__withLocalNavigation__rjTJ_ prc-Stack-Stack-UQ9k6" data-gap="condensed" data-direction="horizontal" data-align="stretch" data-wrap="nowrap" data-justify="start" data-padding="normal"><nav class="styles-module__contextRegion__VbSp2 prc-Breadcrumbs-BreadcrumbsBase-3Gb-B" aria-label="Breadcrumbs" data-overflow="menu" data-variant="normal"><ol class="prc-Breadcrumbs-BreadcrumbsList-BKjpe"><li class="prc-Breadcrumbs-ItemWrapper-k0NLn"><a class="styles-module__contextCrumb__IzGIq prc-Breadcrumbs-Item-jcraJ" href="https://github.com/khavadim1-cyber"><span class="">khavadim1-cyber</span></a></li><li class="prc-Breadcrumbs-ItemWrapper-k0NLn"><a class="styles-module__contextCrumb__IzGIq prc-Breadcrumbs-Item-jcraJ" href="https://github.com/khavadim1-cyber/pp2_v_kha"><span class="styles-module__contextCrumbLast__tI2e3">pp2_v_kha</span></a></li></ol></nav><div class="Search-module__searchButtonGroup__aetw5 prc-ButtonGroup-ButtonGroup-vFUrY"><div><a type="button" aria-label="Search or jump to…" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ Search-module__searchButton__aiE0a" data-loading="false" data-size="medium" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3"><span class="Search-module__placeholder__p9hbG Search-module__text__veSYi Search-module__value__TFoak">Type <kbd class="Search-module__kbd__WCskr">/</kbd> to search</span></span></span></a></div><div></div></div><button data-component="IconButton" type="button" data-hotkey="s,/" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ Search-module__smallSearchButton___8Gvn prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_l9b_"><svg aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" popover="auto"><span id="_R_l9b_">Search or jump to…<span class="prc-src-InternalVisuallyHidden-2YaI6">(<!-- -->s,/<!-- -->)</span></span><span class="prc-TooltipV2-KeybindingHintContainer-Ymj-3 prc-TooltipV2-HasTextBefore-fdOXj" aria-hidden="true"><kbd class="prc-KeybindingHint-KeybindingHint-qpYIs prc-Text-Text-9mHv3" data-testid="keybinding-hint"><span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">s,/</span><span aria-hidden="true">S,/</span></span></kbd></span></span><div class="d-none"><qbsearch-input class="search-input" data-scope="repo:khavadim1-cyber/pp2_v_kha" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="K2KJAkW0Fe-Tmt1TD7VE-rwQ1EHHxJxEEomvZP_8_xrdyC7HzbF7NZ9J8l_joviZ_VVa__NTMb2P2HOIRWxvDg" data-max-custom-scopes="10" data-header-redesign-enabled="true" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="khavadim1-cyber/pp2_v_kha" data-current-org="" data-current-owner="khavadim1-cyber" data-logged-in="true" data-copilot-chat-enabled="true" data-nl-search-enabled="false" data-catalyst="">
  <div class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center height-auto color-bg-transparent border-0 color-fg-subtle mx-0" data-action="click:qbsearch-input#searchInputContainerClicked">

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay="">
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-medium Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-absolute width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container" style="border-radius: 12px;" data-target="qbsearch-input.queryBuilderContainer" hidden="">
          <!-- '"` --><!-- </textarea></xmp> --><form id="query-builder-test-form" action="https://github.com/khavadim1-cyber/pp2_v_kha/blob/main/practise3/classes/class_defenition.py" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder" data-min-width="300" data-catalyst="">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div class="QueryBuilder-StyledInput width-fit " data-target="query-builder.styledInput">
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div aria-hidden="true" class="QueryBuilder-StyledInputContent" data-target="query-builder.styledInputContent"></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"><span></span></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-d04b2b2c-f5ab-4c77-bf75-d3ec3f7fee99" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" aria-controls="query-builder-test-results" aria-autocomplete="list" aria-haspopup="listbox" style="width: 300px;">
          </div>
        </div>
          <span class="sr-only" id="query-builder-test-clear">Clear</span>
          <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-target="query-builder.clearButton" data-action="
                click:query-builder#clear
                focus:query-builder#clearButtonFocus
                blur:query-builder#clearButtonBlur
              " variant="small" hidden="" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

      </div>
      <template id="search-icon"></template>

<template id="code-icon"></template>

<template id="file-code-icon"></template>

<template id="history-icon"></template>

<template id="repo-icon"></template>

<template id="bookmark-icon"></template>

<template id="plus-circle-icon"></template>

<template id="circle-icon"></template>

<template id="trash-icon"></template>

<template id="team-icon"></template>

<template id="project-icon"></template>

<template id="pencil-icon"></template>

<template id="copilot-icon"></template>

<template id="copilot-error-icon"></template>

<template id="workflow-icon"></template>

<template id="book-icon"></template>

<template id="code-review-icon"></template>

<template id="codespaces-icon"></template>

<template id="comment-icon"></template>

<template id="comment-discussion-icon"></template>

<template id="organization-icon"></template>

<template id="rocket-icon"></template>

<template id="shield-check-icon"></template>

<template id="heart-icon"></template>

<template id="server-icon"></template>

<template id="globe-icon"></template>

<template id="issue-opened-icon"></template>

<template id="device-mobile-icon"></template>

<template id="package-icon"></template>

<template id="credit-card-icon"></template>

<template id="play-icon"></template>

<template id="gift-icon"></template>

<template id="code-square-icon"></template>

<template id="device-desktop-icon"></template>

        <div class="position-relative">
                        <ul role="listbox" class="ActionListWrap QueryBuilder-ListWrap" aria-label="Suggestions" data-action="
                combobox-commit:query-builder#comboboxCommit
                mousedown:query-builder#resultsMousedown
              " data-target="query-builder.resultsList" data-persist-list="false" id="query-builder-test-results" tabindex="-1"></ul>

        </div>
      <div class="FormControl-inlineValidation" id="validation-d04b2b2c-f5ab-4c77-bf75-d3ec3f7fee99" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only">0 suggestions.</div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">Search syntax tips</a>            <div class="d-flex flex-1"></div>
              <button data-action="click:qbsearch-input#showFeedbackDialog" type="button" data-view-component="true" class="Button--link Button--medium Button color-fg-accent text-normal ml-2">  <span class="Button-content">
    <span class="Button-label">Give feedback</span>
  </span>
</button>
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden="" data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<dialog-helper>
  <dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="feedback-dialog" aria-modal="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="feedback-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --><form id="code-search-feedback-form" data-turbo="false" action="https://github.com/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="aBSyVruBgI9eJIe6fKxL0VbEEJfRrS7hBs48-ACYwIibNqnr9KKbAtwrmVT0GaF-0JQiE2llq5a6u874piGofw">
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</dialog></dialog-helper>

    <custom-scopes data-target="qbsearch-input.customScopesManager" data-catalyst="">
    
<dialog-helper>
  <dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="custom-scopes-dialog" aria-modal="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="custom-scopes-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden="" class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --><form id="custom-scopes-dialog-form" data-turbo="false" action="https://github.com/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="3jrZ3aQFdqHRPmoCqv5NRrSXm-UqJ18mRWSMwjv-hwCOYj_mhOc7d19_NV2gTNDdhD0zLhya9AL6d1SkG3eKBg">
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required="">
              <input type="text" name="custom_scope_name" id="custom_scope_name" data-target="custom-scopes.customScopesNameField" class="form-control" autocomplete="off" placeholder="github-ruby" required="" maxlength="50" spellcheck="false">
              <input type="hidden" value="eLuaoawPk7ZWVfr5SuVMQfBPRu3R2rTlFH2Thi4tS-tjpjCHbzz0PwmkxqfU4Ek1auYW0k--2zTBRlNbU5sJ3w" data-csrf="true">
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input type="text" name="custom_scope_query" id="custom_scope_query" data-target="custom-scopes.customScopesQueryField" class="form-control" autocomplete="off" placeholder="(repo:mona/a OR repo:mona/b) AND lang:python" required="" maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</dialog></dialog-helper>
    </custom-scopes>
  </div>
</qbsearch-input><input type="hidden" value="xD7Ecz1ALx0I9660aCujNgcYevRaJSf_ntXMvIlcWbGn_4kBJG5hHv37cHHl4ez-rMaHKC9kHiQHg3i0YhsvuQ" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf"></div></div><div data-testid="top-nav-right" class="styles-module__right__mlBQg styles-module__withLocalNavigation__rjTJ_ prc-Stack-Stack-UQ9k6" data-gap="condensed" data-direction="horizontal" data-align="center" data-wrap="nowrap" data-justify="start" data-padding="normal"><div data-testid="top-bar-actions" class="hide-sm hide-md prc-Stack-Stack-UQ9k6" data-gap="condensed" data-direction="horizontal" data-align="center" data-wrap="nowrap" data-justify="start" data-padding="none"><span><div class="prc-ButtonGroup-ButtonGroup-vFUrY"><div><a data-component="IconButton" type="button" href="https://github.com/copilot" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_kjpb_"><svg aria-hidden="true" focusable="false" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id="_R_kjpb_" popover="auto">Chat with Copilot</span></div><div><div class="d-none"></div><button type="button" aria-label="Open Copilot…" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ CopilotItems-module__CopilotMenu__DVdfE" data-loading="false" data-size="medium" data-variant="invisible" id="_R_54jpb_"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path></svg></span></span><span data-component="trailingAction" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></button></div></div><div class="CopilotChat-module__CopilotChatContainer__qrVEG"></div><div class="PortalContainerUtils-module__chatPortalContainer__ZwauZ"></div><div class="PortalContainerUtils-module__menuPortalContainer__q0Ygl CopilotChat-module__menuPortalContainer__DqZy4"></div></span><div class="styles-module__itemDivider__nunbs"></div><button type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk GlobalCreateMenu-module__actionMenuButton__Hj_iB" data-loading="false" data-size="medium" data-variant="invisible" aria-labelledby="global-create-menu-tooltip-_R_1jpb_" id="_R_5jpb_"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-plus" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg></span></span><span data-component="trailingAction" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id="global-create-menu-tooltip-_R_1jpb_" popover="auto">Create new...</span><a data-component="IconButton" type="button" href="https://github.com/issues" data-hotkey="g i" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_63pb_"><svg aria-hidden="true" focusable="false" class="octicon octicon-issue-opened" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" popover="auto" style="top: 52px; left: 1284.39px;"><span id="_R_63pb_">Issues<span class="prc-src-InternalVisuallyHidden-2YaI6">(<!-- -->g then i<!-- -->)</span></span><span class="prc-TooltipV2-KeybindingHintContainer-Ymj-3 prc-TooltipV2-HasTextBefore-fdOXj" aria-hidden="true"><kbd class="prc-KeybindingHint-KeybindingHint-qpYIs prc-Text-Text-9mHv3" data-testid="keybinding-hint"><span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">g</span><span aria-hidden="true">G</span></span><span class="prc-src-InternalVisuallyHidden-2YaI6">then</span> <span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">i</span><span aria-hidden="true">I</span></span></kbd></span></span><a data-component="IconButton" type="button" href="https://github.com/pulls" data-hotkey="g p" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_a3pb_"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-pull-request" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" popover="auto" style="top: 52px; left: 1306.43px;"><span id="_R_a3pb_">Pull requests<span class="prc-src-InternalVisuallyHidden-2YaI6">(<!-- -->g then p<!-- -->)</span></span><span class="prc-TooltipV2-KeybindingHintContainer-Ymj-3 prc-TooltipV2-HasTextBefore-fdOXj" aria-hidden="true"><kbd class="prc-KeybindingHint-KeybindingHint-qpYIs prc-Text-Text-9mHv3" data-testid="keybinding-hint"><span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">g</span><span aria-hidden="true">G</span></span><span class="prc-src-InternalVisuallyHidden-2YaI6">then</span> <span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">p</span><span aria-hidden="true">P</span></span></kbd></span></span><a data-component="IconButton" type="button" href="https://github.com/repos" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_e3pb_"><svg aria-hidden="true" focusable="false" class="octicon octicon-repo" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id="_R_e3pb_" popover="auto">Repositories</span></div><a data-component="IconButton" type="button" href="https://github.com/notifications" data-hotkey="g n" class="prc-Button-ButtonBase-9n-Xk styles-module__appHeaderButton__axedQ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_5pb_"><svg aria-hidden="true" focusable="false" class="octicon octicon-inbox" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2.8 2.06A1.75 1.75 0 0 1 4.41 1h7.18c.7 0 1.333.417 1.61 1.06l2.74 6.395c.04.093.06.194.06.295v4.5A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25v-4.5c0-.101.02-.202.06-.295Zm1.61.44a.25.25 0 0 0-.23.152L1.887 8H4.75a.75.75 0 0 1 .6.3L6.625 10h2.75l1.275-1.7a.75.75 0 0 1 .6-.3h2.863L11.82 2.652a.25.25 0 0 0-.23-.152Zm10.09 7h-2.875l-1.275 1.7a.75.75 0 0 1-.6.3h-3.5a.75.75 0 0 1-.6-.3L4.375 9.5H1.5v3.75c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" popover="auto"><span id="_R_5pb_">You have no unread notifications<span class="prc-src-InternalVisuallyHidden-2YaI6">(<!-- -->g then n<!-- -->)</span></span><span class="prc-TooltipV2-KeybindingHintContainer-Ymj-3 prc-TooltipV2-HasTextBefore-fdOXj" aria-hidden="true"><kbd class="prc-KeybindingHint-KeybindingHint-qpYIs prc-Text-Text-9mHv3" data-testid="keybinding-hint"><span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">g</span><span aria-hidden="true">G</span></span><span class="prc-src-InternalVisuallyHidden-2YaI6">then</span> <span class="prc-components-Chord-DdhWN prc-components-ChordOnEmphasis-O-4BS prc-components-ChordSmall-c-P-x prc-Text-Text-9mHv3" data-kbd-chord="true"> <span class="prc-src-InternalVisuallyHidden-2YaI6">n</span><span aria-hidden="true">N</span></span></kbd></span></span><div class="GlobalNavUserMenu-module__container__NaVIt"><button data-component="IconButton" type="button" aria-haspopup="menu" data-login="serikkalijanaris-cyber" class="prc-Button-ButtonBase-9n-Xk GlobalNavUserMenu-module__anchor__Dcej6 prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_2npb_"><img data-component="Avatar" class="Box-sc-62in7e-0 lpqgUB prc-Avatar-Avatar-0xaUi" alt="User avatar" width="32" height="32" style="--avatarSize-regular:32px" src="./def_files/257359913" data-testid="github-avatar"></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id="_R_2npb_" popover="auto">Open user navigation menu</span></div></div></div><h2 class="prc-src-InternalVisuallyHidden-2YaI6">Repository navigation</h2><nav class="prc-components-UnderlineWrapper-eT-Yj LocalNavigation-module__LocalNavigation__b0Xc0" aria-label="Repository" data-variant="inset"><ul class="prc-components-UnderlineItemList-xKlKC" role="list"><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/khavadim1-cyber/pp2_v_kha" aria-current="page" data-hotkey="g c" data-react-nav="code-view" data-react-nav-anchor="code-view-repo-link" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-code" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path></svg></span><span data-component="text" data-content="Code">Code</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/khavadim1-cyber/pp2_v_kha/issues" data-hotkey="g i" data-react-nav="issues-react" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-issue-opened" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path></svg></span><span data-component="text" data-content="Issues">Issues</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/khavadim1-cyber/pp2_v_kha/pulls" data-hotkey="g p" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-pull-request" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path></svg></span><span data-component="text" data-content="Pull requests">Pull requests</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/khavadim1-cyber/pp2_v_kha/agents?author=serikkalijanaris-cyber" data-hotkey="g e" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-agent" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M14.5 8.9v-.052A2.956 2.956 0 0 0 11.542 5.9a.815.815 0 0 1-.751-.501l-.145-.348A3.496 3.496 0 0 0 7.421 2.9h-.206a3.754 3.754 0 0 0-3.736 4.118l.011.121a.822.822 0 0 1-.619.879A1.81 1.81 0 0 0 1.5 9.773v.14c0 1.097.89 1.987 1.987 1.987H4.5a.75.75 0 0 1 0 1.5H3.487A3.487 3.487 0 0 1 0 9.913v-.14C0 8.449.785 7.274 1.963 6.75A5.253 5.253 0 0 1 7.215 1.4h.206a4.992 4.992 0 0 1 4.586 3.024A4.455 4.455 0 0 1 16 8.848V8.9a.75.75 0 0 1-1.5 0Z"></path><path d="m8.38 7.67 2.25 2.25a.749.749 0 0 1 0 1.061L8.38 13.23a.749.749 0 1 1-1.06-1.06l1.719-1.72L7.32 8.731A.75.75 0 0 1 8.38 7.67ZM15 13.45h-3a.75.75 0 0 1 0-1.5h3a.75.75 0 0 1 0 1.5Z"></path></svg></span><span data-component="text" data-content="Agents">Agents</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/khavadim1-cyber/pp2_v_kha/actions" data-hotkey="g a" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-play" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path></svg></span><span data-component="text" data-content="Actions">Actions</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/khavadim1-cyber/pp2_v_kha/projects" data-hotkey="g b" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-table" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path></svg></span><span data-component="text" data-content="Projects">Projects</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/khavadim1-cyber/pp2_v_kha/security" data-hotkey="g s" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-shield" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path></svg></span><span data-component="text" data-content="Security">Security</span></a></li><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/khavadim1-cyber/pp2_v_kha/pulse" data-turbo-frame="repo-content-turbo-frame" class="prc-components-UnderlineItem-7fP-n" data-discover="true"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-graph" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path></svg></span><span data-component="text" data-content="Insights">Insights</span></a></li></ul></nav></header><script type="application/json" id="__PRIMER_DATA__R_0___">{"resolvedServerColorMode":"night"}</script></div>
</react-partial>


      <div class="js-global-bar" style="display: none;">
        


<qbsearch-input class="search-input" data-scope="repo:khavadim1-cyber/pp2_v_kha" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="K2KJAkW0Fe-Tmt1TD7VE-rwQ1EHHxJxEEomvZP_8_xrdyC7HzbF7NZ9J8l_joviZ_VVa__NTMb2P2HOIRWxvDg" data-max-custom-scopes="10" data-header-redesign-enabled="true" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="khavadim1-cyber/pp2_v_kha" data-current-org="" data-current-owner="khavadim1-cyber" data-logged-in="true" data-copilot-chat-enabled="true" data-nl-search-enabled="false" data-catalyst="">
  <div class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center height-auto color-bg-transparent border-0 color-fg-subtle mx-0" data-action="click:qbsearch-input#searchInputContainerClicked">

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay="">
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-medium Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-absolute width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container" style="border-radius: 12px;" data-target="qbsearch-input.queryBuilderContainer" hidden="">
          <!-- '"` --><!-- </textarea></xmp> --><form id="query-builder-test-form" action="https://github.com/khavadim1-cyber/pp2_v_kha/blob/main/practise3/classes/class_defenition.py" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder" data-min-width="300" data-catalyst="">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div class="QueryBuilder-StyledInput width-fit " data-target="query-builder.styledInput">
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div aria-hidden="true" class="QueryBuilder-StyledInputContent" data-target="query-builder.styledInputContent"></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"><span></span></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-d04b2b2c-f5ab-4c77-bf75-d3ec3f7fee99" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" aria-controls="query-builder-test-results" aria-autocomplete="list" aria-haspopup="listbox" style="width: 300px;">
          </div>
        </div>
          <span class="sr-only" id="query-builder-test-clear">Clear</span>
          <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-target="query-builder.clearButton" data-action="
                click:query-builder#clear
                focus:query-builder#clearButtonFocus
                blur:query-builder#clearButtonBlur
              " variant="small" hidden="" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

      </div>
      <template id="search-icon"></template>

<template id="code-icon"></template>

<template id="file-code-icon"></template>

<template id="history-icon"></template>

<template id="repo-icon"></template>

<template id="bookmark-icon"></template>

<template id="plus-circle-icon"></template>

<template id="circle-icon"></template>

<template id="trash-icon"></template>

<template id="team-icon"></template>

<template id="project-icon"></template>

<template id="pencil-icon"></template>

<template id="copilot-icon"></template>

<template id="copilot-error-icon"></template>

<template id="workflow-icon"></template>

<template id="book-icon"></template>

<template id="code-review-icon"></template>

<template id="codespaces-icon"></template>

<template id="comment-icon"></template>

<template id="comment-discussion-icon"></template>

<template id="organization-icon"></template>

<template id="rocket-icon"></template>

<template id="shield-check-icon"></template>

<template id="heart-icon"></template>

<template id="server-icon"></template>

<template id="globe-icon"></template>

<template id="issue-opened-icon"></template>

<template id="device-mobile-icon"></template>

<template id="package-icon"></template>

<template id="credit-card-icon"></template>

<template id="play-icon"></template>

<template id="gift-icon"></template>

<template id="code-square-icon"></template>

<template id="device-desktop-icon"></template>

        <div class="position-relative">
                        <ul role="listbox" class="ActionListWrap QueryBuilder-ListWrap" aria-label="Suggestions" data-action="
                combobox-commit:query-builder#comboboxCommit
                mousedown:query-builder#resultsMousedown
              " data-target="query-builder.resultsList" data-persist-list="false" id="query-builder-test-results" tabindex="-1"></ul>

        </div>
      <div class="FormControl-inlineValidation" id="validation-d04b2b2c-f5ab-4c77-bf75-d3ec3f7fee99" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only">0 suggestions.</div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">Search syntax tips</a>            <div class="d-flex flex-1"></div>
              <button data-action="click:qbsearch-input#showFeedbackDialog" type="button" data-view-component="true" class="Button--link Button--medium Button color-fg-accent text-normal ml-2">  <span class="Button-content">
    <span class="Button-label">Give feedback</span>
  </span>
</button>
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden="" data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<dialog-helper>
  <dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="feedback-dialog" aria-modal="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="feedback-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --><form id="code-search-feedback-form" data-turbo="false" action="https://github.com/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="aBSyVruBgI9eJIe6fKxL0VbEEJfRrS7hBs48-ACYwIibNqnr9KKbAtwrmVT0GaF-0JQiE2llq5a6u874piGofw">
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</dialog></dialog-helper>

    <custom-scopes data-target="qbsearch-input.customScopesManager" data-catalyst="">
    
<dialog-helper>
  <dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="custom-scopes-dialog" aria-modal="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="custom-scopes-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden="" class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --><form id="custom-scopes-dialog-form" data-turbo="false" action="https://github.com/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="3jrZ3aQFdqHRPmoCqv5NRrSXm-UqJ18mRWSMwjv-hwCOYj_mhOc7d19_NV2gTNDdhD0zLhya9AL6d1SkG3eKBg">
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required="">
              <input type="text" name="custom_scope_name" id="custom_scope_name" data-target="custom-scopes.customScopesNameField" class="form-control" autocomplete="off" placeholder="github-ruby" required="" maxlength="50" spellcheck="false">
              <input type="hidden" value="eLuaoawPk7ZWVfr5SuVMQfBPRu3R2rTlFH2Thi4tS-tjpjCHbzz0PwmkxqfU4Ek1auYW0k--2zTBRlNbU5sJ3w" data-csrf="true">
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input type="text" name="custom_scope_query" id="custom_scope_query" data-target="custom-scopes.customScopesQueryField" class="form-control" autocomplete="off" placeholder="(repo:mona/a OR repo:mona/b) AND lang:python" required="" maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</dialog></dialog-helper>
    </custom-scopes>
  </div>
</qbsearch-input>  <input type="hidden" value="xD7Ecz1ALx0I9660aCujNgcYevRaJSf_ntXMvIlcWbGn_4kBJG5hHv37cHHl4ez-rMaHKC9kHiQHg3i0YhsvuQ" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf">


      </div>


      <div hidden="hidden" data-view-component="true" class="js-stale-session-flash stale-session-flash flash flash-warn flash-full">
  
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span class="js-stale-session-flash-signed-in" hidden="">You signed in with another tab or window. <a class="Link--inTextBlock" href="https://github.com/khavadim1-cyber/pp2_v_kha/blob/main/practise3/classes/class_defenition.py">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-signed-out" hidden="">You signed out in another tab or window. <a class="Link--inTextBlock" href="https://github.com/khavadim1-cyber/pp2_v_kha/blob/main/practise3/classes/class_defenition.py">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-switched" hidden="">You switched accounts on another tab or window. <a class="Link--inTextBlock" href="https://github.com/khavadim1-cyber/pp2_v_kha/blob/main/practise3/classes/class_defenition.py">Reload</a> to refresh your session.</span>

    <button id="icon-button-d34124ba-89df-4a1d-aa5d-e436aae7ddba" aria-labelledby="tooltip-11deefeb-fdb9-4fe8-95eb-d13d5d75fb8d" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium flash-close js-flash-close">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-11deefeb-fdb9-4fe8-95eb-d13d5d75fb8d" for="icon-button-d34124ba-89df-4a1d-aa5d-e436aae7ddba" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Dismiss alert</tool-tip>


  
</div>
        
          
    </div>

  <div id="start-of-content" class="show-on-focus"></div>








    <div id="js-flash-container" class="flash-container" data-turbo-replace="">




  <template class="js-flash-template"></template>
</div>


    
  <notification-shelf-watcher data-base-url="https://github.com/notifications/beta/shelf" data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MjU3MzU5OTEzIiwidCI6MTc3MTI3MTIxM30=--d8e1c2f198e620220c378f3f6a0248aa8a63eb6258ed10969bf77065c0d954ea" data-view-component="true" class="js-socket-channel" data-refresh-delay="500" data-catalyst="" data-throttle-delay="5000"></notification-shelf-watcher>
  <div hidden="" data-initial="" data-target="notification-shelf-watcher.placeholder"></div>






  <div class="application-main " data-commit-hovercards-enabled="" data-discussion-hovercards-enabled="" data-issue-and-pr-hovercards-enabled="" data-project-hovercards-enabled="">
        <div itemscope="" itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container">
      
  


<template class="js-user-list-create-dialog-template" data-label="Create list"></template>



    






  
    

  <div id="repository-container-header" data-turbo-replace="" hidden=""></div>



<turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="" src="https://github.com/khavadim1-cyber/pp2_v_kha/tree/main/practise3" complete=""><react-app app-name="react-code-view" initial-path="/khavadim1-cyber/pp2_v_kha/tree/main/practise3" style="display: block; min-height: calc(100vh - 64px);" data-attempted-ssr="true" data-ssr="true" data-lazy="false" data-alternate="false" data-data-router-enabled="false" data-react-profiling="true" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-app.embeddedData">{"payload":{"allShortcutsEnabled":true,"path":"practise3","repo":{"id":1138022152,"defaultBranch":"main","name":"pp2_v_kha","ownerLogin":"khavadim1-cyber","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2026-01-20T11:27:36.000+05:00","ownerAvatar":"https://avatars.githubusercontent.com/u/230659265?v=4","public":true,"private":false,"isOrgOwned":false},"currentUser":{"id":257359913,"login":"serikkalijanaris-cyber","userEmail":"serikkalijanaris@gmail.com"},"refInfo":{"name":"main","listCacheKey":"v0:1768897298.0","canEdit":true,"refType":"branch","currentOid":"6b80b92c8c1121c12d9e079d40aab8c5ce965ad2"},"tree":{"items":[{"name":"classes","path":"practise3/classes","contentType":"directory"},{"name":"functions","path":"practise3/functions","contentType":"directory"},{"name":"inheritance","path":"practise3/inheritance","contentType":"directory"},{"name":"lambda","path":"practise3/lambda","contentType":"directory"}],"totalCount":4,"templateDirectorySuggestionUrl":null,"readme":null,"showBranchInfobar":false},"fileTree":{"":{"items":[{"name":"practise1","path":"practise1","contentType":"directory"},{"name":"practise2","path":"practise2","contentType":"directory"},{"name":"practise3","path":"practise3","contentType":"directory"},{"name":"practise4","path":"practise4","contentType":"directory"},{"name":".DS_Store","path":".DS_Store","contentType":"file"}],"totalCount":5}},"fileTreeProcessingTime":5.717478,"foldersToFetch":[],"userNameDisplayConfiguration":null,"treeExpanded":true,"symbolsExpanded":false,"copilotSWEAgentEnabled":false,"csrf_tokens":{"/khavadim1-cyber/pp2_v_kha/branches":{"post":"uxUDDKZrAsh53C_s3WGTd7w-yOeYewMtPRq5qwLwEjEvEBm8mQ3aGA-WWh85F9QkRacQpvEVJ8zx-zWWt3OQBQ"},"/khavadim1-cyber/pp2_v_kha/branches/fetch_and_merge/main":{"post":"JcvEXVWmGrSYGGRZCtLQlj6fvPa6QV8Wz6tM8Mfa-Ef-DqexEaXpuiJ2kdl9FTG8Cw_fuSCO0IeKs1ZPigODqg"},"/khavadim1-cyber/pp2_v_kha/branches/fetch_and_merge/main?discard_changes=true":{"post":"9eGk6tbFCmj_ndPxMKIhAVIEu7KIKSzw2LMP1brMW2wuJMcGksb5ZkXzJnFHZcArZ5TY_RLmo2GdqxVq9xUggQ"}}},"title":"pp2_v_kha/practise3 at main · khavadim1-cyber/pp2_v_kha","appPayload":{"helpUrl":"https://docs.github.com","findFileWorkerPath":"/assets-cdn/worker/find-file-worker-59333858d672c62a.js","findInFileWorkerPath":"/assets-cdn/worker/find-in-file-worker-2df305454d6b4737.js","githubDevUrl":"https://github.dev/","enabled_features":{"code_nav_ui_events":false,"react_blob_overlay":true,"copilot_mission_control_decoupled_mode":false}}}</script>
  <div data-target="react-app.reactRoot"><meta name="github-code-view-meta-stats" id="github-code-view-meta-stats" data-hydrostats="publish"> <!-- --> <!-- --> <button hidden="" data-testid="header-permalink-button" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="y,Shift+Y"></button><button hidden="" data-hotkey="y,Shift+Y"></button><div><div style="--spacing:var(--spacing-none)" class="prc-PageLayout-PageLayoutRoot--KH-d"><div class="prc-PageLayout-PageLayoutWrapper-2BhU2" data-width="full"><div class="prc-PageLayout-PageLayoutContent-BneH9"><div tabindex="0" class="Box-sc-62in7e-0 jmjlbk"><div class="prc-PageLayout-PaneWrapper-pHPop ReposFileTreePane-module__Pane__rBZpI ReposFileTreePane-module__HidePane__VHAVt" style="--offset-header:0px;--spacing-row:var(--spacing-none);--spacing-column:var(--spacing-none)" data-is-hidden="false" data-position="start" data-sticky="true"><div class="prc-PageLayout-HorizontalDivider-JLVqp prc-PageLayout-PaneHorizontalDivider-9tbnE" data-variant-regular="none" data-variant-narrow="none" data-position="start" style="--spacing-divider:var(--spacing-none);--spacing:var(--spacing-none)"></div><div class="prc-PageLayout-Pane-AyzHK" data-resizable="true" style="--spacing: var(--spacing-none); --pane-min-width: 256px; --pane-max-width: 577px; --pane-width-size: var(--pane-width-large); --pane-width: 320px;"><div><div id="repos-file-tree" class="ReposFileTreePane-module__PaneContents__SJjfF"><div class="ReposFileTreePane-module__Box_1__PpIop"><div class="Box-sc-62in7e-0 fvNWEZ"><h2 class="use-tree-pane-module__Heading__s4QbZ prc-Heading-Heading-MtWFE"><button data-component="IconButton" type="button" data-testid="collapse-file-tree-button" aria-expanded="true" aria-controls="repos-file-tree" class="prc-Button-ButtonBase-9n-Xk position-relative ExpandFileTreeButton-module__expandButton__hDOcv fgColor-muted prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible" aria-labelledby="_R_156mplab_" data-hotkey="Control+b"><svg aria-hidden="true" focusable="false" class="octicon octicon-sidebar-expand" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.177 7.823 2.396-2.396A.25.25 0 0 1 7 5.604v4.792a.25.25 0 0 1-.427.177L4.177 8.177a.25.25 0 0 1 0-.354Z"></path><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25H9.5v-13Zm12.5 13a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11v13Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="se" aria-hidden="true" id="_R_156mplab_" popover="auto">Collapse file tree</span><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+b"></button></h2><h2 class="Heading-sc-1vc165i-0 dWfbpP">Files</h2></div><div class="ReposFileTreePane-module__Box_2__g74WI"><div class="ReposFileTreePane-module__Box_3__D6cTp"><button type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" style="min-width:0" aria-label="main branch" data-testid="anchor-button" class="prc-Button-ButtonBase-9n-Xk react-repos-tree-pane-ref-selector width-full ref-selector-class RefSelectorAnchoredOverlay-module__RefSelectorOverlayBtn__a3WK3" data-loading="false" data-size="medium" data-variant="default" id="ref-picker-repos-header-ref-selector" data-hotkey="w"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3"><div class="RefSelectorAnchoredOverlay-module__RefSelectorOverlayContainer__yaf4p"><div class="RefSelectorAnchoredOverlay-module__RefSelectorOverlayHeader__XtXRG"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="ref-selector-button-text-container RefSelectorAnchoredOverlay-module__RefSelectorBtnTextContainer__Di3rk"><span class="RefSelectorAnchoredOverlay-module__RefSelectorText__w_fmP">&nbsp;<!-- -->main</span></div></div></span><span data-component="trailingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-testid="ref-selector-hotkey-button" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="w"></button></div><div class="ReposFileTreePane-module__Box_4__DG4pa"><a data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk ReposFileTreePane-module__IconButton__rGggU prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-labelledby="_R_q6mplab_" href="https://github.com/khavadim1-cyber/pp2_v_kha/new/main/practise3/classes" data-discover="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-plus" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="n" aria-hidden="true" id="_R_q6mplab_" popover="auto">Add file</span><button data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk SearchButton-module__IconButton__SBlqu ReposFileTreePane-module__SearchButtonWithLeftBorder__TBrDc prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-labelledby="_R_3a6mplab_" data-hotkey="/"><svg aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="nw" aria-hidden="true" id="_R_3a6mplab_" popover="auto">Search this repository</span><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="/"></button></div></div></div><div class="Box-sc-62in7e-0 ReposFileTreePane-module__FileResultsList__zmSnM"><span class="TextInput__StyledTextInput-sc-ttxlvl-0 d-flex FileResultsList-module__FilesSearchBox__ivVkc TextInput-wrapper prc-components-TextInputWrapper-Hpdqi prc-components-TextInputBaseWrapper-wY-n0" data-leading-visual="true" data-trailing-visual="true" aria-busy="false"><span class="TextInput-icon" id="_R_5amplab_" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></span><input type="text" aria-label="Go to file" role="combobox" aria-controls="file-results-list" aria-expanded="false" aria-haspopup="dialog" autocorrect="off" spellcheck="false" placeholder="Go to file" aria-describedby="_R_5amplab_ _R_5amplabH1_" data-component="input" class="prc-components-Input-IwWrt" value=""><span class="TextInput-icon" id="_R_5amplabH1_" aria-hidden="true"><kbd>t</kbd></span></span></div><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="t,Shift+T"></button><button hidden="" data-hotkey="t,Shift+T"></button><div class="ReposFileTreePane-module__Box_8__TLAjy"></div><div class="ReposFileTreePane-module__Box_5__Zy_o6"><div><div class="react-tree-show-tree-items"><div class="ReposFileTreeView-module__Box__vkb5W" data-testid="repos-file-tree-container"><nav aria-label="File Tree Navigation"><span class="prc-src-InternalVisuallyHidden-2YaI6"><div>lambda content loaded</div></span><ul role="tree" aria-label="Files" data-truncate-text="true" class="prc-TreeView-TreeViewRootUlStyles-Mzrmj"><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practise1-item" role="treeitem" aria-labelledby="_r_1j_" aria-describedby="_r_1k_" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-hq3Xq prc-TreeView-TreeViewItemToggleHover-H9tbt prc-TreeView-TreeViewItemToggleEnd-nWt9I"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id="_r_1j_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_1k_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-yP1oY"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>practise1</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practise2-item" role="treeitem" aria-labelledby="_r_1n_" aria-describedby="_r_1o_" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-hq3Xq prc-TreeView-TreeViewItemToggleHover-H9tbt prc-TreeView-TreeViewItemToggleEnd-nWt9I"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id="_r_1n_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_1o_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-yP1oY"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>practise2</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practise3-item" role="treeitem" aria-labelledby="_r_1r_" aria-describedby="_r_1s_" aria-level="1" aria-expanded="true" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-hq3Xq prc-TreeView-TreeViewItemToggleHover-H9tbt prc-TreeView-TreeViewItemToggleEnd-nWt9I"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-down" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M6 8.825c-.2 0-.4-.1-.5-.2l-3.3-3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l2.7 2.7 2.7-2.7c.3-.3.8-.3 1.1 0 .3.3.3.8 0 1.1l-3.2 3.2c-.2.2-.4.3-.6.3Z"></path></svg></div><div id="_r_1r_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_1s_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-yP1oY"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-open-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M.513 1.513A1.75 1.75 0 0 1 1.75 1h3.5c.55 0 1.07.26 1.4.7l.9 1.2a.25.25 0 0 0 .2.1H13a1 1 0 0 1 1 1v.5H2.75a.75.75 0 0 0 0 1.5h11.978a1 1 0 0 1 .994 1.117L15 13.25A1.75 1.75 0 0 1 13.25 15H1.75A1.75 1.75 0 0 1 0 13.25V2.75c0-.464.184-.91.513-1.237Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>practise3</span></span></div></div><ul role="group" aria-label="practise3" style="list-style: none; padding: 0px; margin: 0px;"><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practise3/classes-item" role="treeitem" aria-labelledby="_r_1v_" aria-describedby="_r_20_" aria-level="2" aria-expanded="true" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover prc-TreeView-TreeViewItemToggle-hq3Xq prc-TreeView-TreeViewItemToggleHover-H9tbt prc-TreeView-TreeViewItemToggleEnd-nWt9I"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-down" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M6 8.825c-.2 0-.4-.1-.5-.2l-3.3-3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l2.7 2.7 2.7-2.7c.3-.3.8-.3 1.1 0 .3.3.3.8 0 1.1l-3.2 3.2c-.2.2-.4.3-.6.3Z"></path></svg></div><div id="_r_1v_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_20_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-yP1oY"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-open-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M.513 1.513A1.75 1.75 0 0 1 1.75 1h3.5c.55 0 1.07.26 1.4.7l.9 1.2a.25.25 0 0 0 .2.1H13a1 1 0 0 1 1 1v.5H2.75a.75.75 0 0 0 0 1.5h11.978a1 1 0 0 1 .994 1.117L15 13.25A1.75 1.75 0 0 1 13.25 15H1.75A1.75 1.75 0 0 1 0 13.25V2.75c0-.464.184-.91.513-1.237Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>classes</span></span></div></div><ul role="group" aria-label="classes" style="list-style: none; padding: 0px; margin: 0px;"><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practise3/classes/class_defenition.py-item" role="treeitem" aria-labelledby="_r_59_" aria-describedby="_r_5a_" aria-level="3" aria-selected="false" aria-current="true"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 3;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_59_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_5a_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>class_defenition.py</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practise3/classes/class_methods.py-item" role="treeitem" aria-labelledby="_r_5d_" aria-describedby="_r_5e_" aria-level="3" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 3; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_5d_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_5e_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>class_methods.py</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practise3/classes/class_variables.py-item" role="treeitem" aria-labelledby="_r_5h_" aria-describedby="_r_5i_" aria-level="3" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 3; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_5h_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_5i_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>class_variables.py</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practise3/classes/init_method.py-item" role="treeitem" aria-labelledby="_r_5l_" aria-describedby="_r_5m_" aria-level="3" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 3; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_5l_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_5m_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>init_method.py</span></span></div></div></li></ul></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practise3/functions-item" role="treeitem" aria-labelledby="_r_23_" aria-describedby="_r_24_" aria-level="2" aria-expanded="true" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover prc-TreeView-TreeViewItemToggle-hq3Xq prc-TreeView-TreeViewItemToggleHover-H9tbt prc-TreeView-TreeViewItemToggleEnd-nWt9I"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-down" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M6 8.825c-.2 0-.4-.1-.5-.2l-3.3-3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l2.7 2.7 2.7-2.7c.3-.3.8-.3 1.1 0 .3.3.3.8 0 1.1l-3.2 3.2c-.2.2-.4.3-.6.3Z"></path></svg></div><div id="_r_23_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_24_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-yP1oY"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-open-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M.513 1.513A1.75 1.75 0 0 1 1.75 1h3.5c.55 0 1.07.26 1.4.7l.9 1.2a.25.25 0 0 0 .2.1H13a1 1 0 0 1 1 1v.5H2.75a.75.75 0 0 0 0 1.5h11.978a1 1 0 0 1 .994 1.117L15 13.25A1.75 1.75 0 0 1 13.25 15H1.75A1.75 1.75 0 0 1 0 13.25V2.75c0-.464.184-.91.513-1.237Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>functions</span></span></div></div><ul role="group" aria-label="functions" style="list-style: none; padding: 0px; margin: 0px;"><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practise3/functions/args_kwargs.py-item" role="treeitem" aria-labelledby="_r_7p_" aria-describedby="_r_7q_" aria-level="3" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 3; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_7p_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_7q_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>args_kwargs.py</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practise3/functions/basic_functions.py-item" role="treeitem" aria-labelledby="_r_7t_" aria-describedby="_r_7u_" aria-level="3" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 3; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_7t_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_7u_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>basic_functions.py</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practise3/functions/function_arguments.py-item" role="treeitem" aria-labelledby="_r_81_" aria-describedby="_r_82_" aria-level="3" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 3; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_81_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_82_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>function_arguments.py</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practise3/functions/return_values.py-item" role="treeitem" aria-labelledby="_r_85_" aria-describedby="_r_86_" aria-level="3" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 3; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_85_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_86_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>return_values.py</span></span></div></div></li></ul></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practise3/inheritance-item" role="treeitem" aria-labelledby="_r_27_" aria-describedby="_r_28_" aria-level="2" aria-expanded="true" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover prc-TreeView-TreeViewItemToggle-hq3Xq prc-TreeView-TreeViewItemToggleHover-H9tbt prc-TreeView-TreeViewItemToggleEnd-nWt9I"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-down" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M6 8.825c-.2 0-.4-.1-.5-.2l-3.3-3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l2.7 2.7 2.7-2.7c.3-.3.8-.3 1.1 0 .3.3.3.8 0 1.1l-3.2 3.2c-.2.2-.4.3-.6.3Z"></path></svg></div><div id="_r_27_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_28_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-yP1oY"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-open-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M.513 1.513A1.75 1.75 0 0 1 1.75 1h3.5c.55 0 1.07.26 1.4.7l.9 1.2a.25.25 0 0 0 .2.1H13a1 1 0 0 1 1 1v.5H2.75a.75.75 0 0 0 0 1.5h11.978a1 1 0 0 1 .994 1.117L15 13.25A1.75 1.75 0 0 1 13.25 15H1.75A1.75 1.75 0 0 1 0 13.25V2.75c0-.464.184-.91.513-1.237Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>inheritance</span></span></div></div><ul role="group" aria-label="inheritance" style="list-style: none; padding: 0px; margin: 0px;"><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practise3/inheritance/inheritance_basics.py-item" role="treeitem" aria-labelledby="_r_8f_" aria-describedby="_r_8g_" aria-level="3" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 3; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_8f_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_8g_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>inheritance_basics.py</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practise3/inheritance/method_overriding.py-item" role="treeitem" aria-labelledby="_r_8j_" aria-describedby="_r_8k_" aria-level="3" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 3; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_8j_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_8k_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>method_overriding.py</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practise3/inheritance/multiple_inheritance.py-item" role="treeitem" aria-labelledby="_r_8n_" aria-describedby="_r_8o_" aria-level="3" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 3; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_8n_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_8o_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>multiple_inheritance.py</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practise3/inheritance/super_function.py-item" role="treeitem" aria-labelledby="_r_8r_" aria-describedby="_r_8s_" aria-level="3" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 3; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_8r_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_8s_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>super_function.py</span></span></div></div></li></ul></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="0" id="practise3/lambda-item" role="treeitem" aria-labelledby="_r_2b_" aria-describedby="_r_2c_" aria-level="2" aria-expanded="true" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 2; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover prc-TreeView-TreeViewItemToggle-hq3Xq prc-TreeView-TreeViewItemToggleHover-H9tbt prc-TreeView-TreeViewItemToggleEnd-nWt9I"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-down" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M6 8.825c-.2 0-.4-.1-.5-.2l-3.3-3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l2.7 2.7 2.7-2.7c.3-.3.8-.3 1.1 0 .3.3.3.8 0 1.1l-3.2 3.2c-.2.2-.4.3-.6.3Z"></path></svg></div><div id="_r_2b_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_2c_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-yP1oY"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-open-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M.513 1.513A1.75 1.75 0 0 1 1.75 1h3.5c.55 0 1.07.26 1.4.7l.9 1.2a.25.25 0 0 0 .2.1H13a1 1 0 0 1 1 1v.5H2.75a.75.75 0 0 0 0 1.5h11.978a1 1 0 0 1 .994 1.117L15 13.25A1.75 1.75 0 0 1 13.25 15H1.75A1.75 1.75 0 0 1 0 13.25V2.75c0-.464.184-.91.513-1.237Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>lambda</span></span></div></div><ul role="group" aria-label="lambda" style="list-style: none; padding: 0px; margin: 0px;"><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practise3/lambda/lambda_basics.py-item" role="treeitem" aria-labelledby="_r_95_" aria-describedby="_r_96_" aria-level="3" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 3; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_95_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_96_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>lambda_basics.py</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practise3/lambda/lambda_with_filter.py-item" role="treeitem" aria-labelledby="_r_99_" aria-describedby="_r_9a_" aria-level="3" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 3; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_99_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_9a_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>lambda_with_filter.py</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practise3/lambda/lambda_with_map.py-item" role="treeitem" aria-labelledby="_r_9d_" aria-describedby="_r_9e_" aria-level="3" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 3; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_9d_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_9e_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>lambda_with_map.py</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practise3/lambda/lambda_with_sorted.py-item" role="treeitem" aria-labelledby="_r_9h_" aria-describedby="_r_9i_" aria-level="3" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 3; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div><div class="PRIVATE_TreeView-item-level-line prc-TreeView-TreeViewItemLevelLine-F-0-2"></div></div></div><div id="_r_9h_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_9i_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>lambda_with_sorted.py</span></span></div></div></li></ul></li></ul></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id="practise4-item" role="treeitem" aria-labelledby="_r_2f_" aria-describedby="_r_2g_" aria-level="1" aria-expanded="false" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div class="PRIVATE_TreeView-item-toggle PRIVATE_TreeView-item-toggle--hover PRIVATE_TreeView-item-toggle--end prc-TreeView-TreeViewItemToggle-hq3Xq prc-TreeView-TreeViewItemToggleHover-H9tbt prc-TreeView-TreeViewItemToggleEnd-nWt9I"><svg aria-hidden="true" focusable="false" class="octicon octicon-chevron-right" viewBox="0 0 12 12" width="12" height="12" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M4.7 10c-.2 0-.4-.1-.5-.2-.3-.3-.3-.8 0-1.1L6.9 6 4.2 3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l3.3 3.2c.3.3.3.8 0 1.1L5.3 9.7c-.2.2-.4.3-.6.3Z"></path></svg></div><div id="_r_2f_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_2g_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><div class="PRIVATE_TreeView-directory-icon prc-TreeView-TreeViewDirectoryIcon-yP1oY"><svg aria-hidden="true" focusable="false" class="octicon octicon-file-directory-fill" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></svg></div></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>practise4</span></span></div></div></li><li class="PRIVATE_TreeView-item prc-TreeView-TreeViewItem-Ter5f" tabindex="-1" id=".DS_Store-item" role="treeitem" aria-labelledby="_r_2j_" aria-describedby="_r_2k_" aria-level="1" aria-selected="false"><div class="PRIVATE_TreeView-item-container prc-TreeView-TreeViewItemContainer-z6qqQ" style="--level: 1; content-visibility: auto; contain-intrinsic-size: auto 2rem;"><div style="grid-area: spacer; display: flex;"><div style="width: 100%; display: flex;"></div></div><div id="_r_2j_" class="PRIVATE_TreeView-item-content prc-TreeView-TreeViewItemContent-RKsCI"><div class="PRIVATE_VisuallyHidden prc-TreeView-TreeViewVisuallyHidden-1N8xK" aria-hidden="true" id="_r_2k_"></div><div class="PRIVATE_TreeView-item-visual prc-TreeView-TreeViewItemVisual-naWzj" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg></div><span class="PRIVATE_TreeView-item-content-text prc-TreeView-TreeViewItemContentText-FFaKp"><span>.DS_Store</span></span></div></div></li></ul></nav></div></div></div></div></div></div></div><div class="prc-PageLayout-VerticalDivider-9QRmK prc-PageLayout-PaneVerticalDivider-le57g" data-variant-narrow="none" data-variant-regular="line" data-variant-wide="line" data-position="start" style="--spacing:var(--spacing-none)"><div class="prc-PageLayout-DraggableHandle-9s6B4" role="slider" aria-label="Draggable pane splitter" aria-valuemin="256" aria-valuemax="577" aria-valuenow="320" aria-valuetext="Pane width 320 pixels" tabindex="0"></div></div></div></div><div class="prc-PageLayout-ContentWrapper-gR9eG" data-is-hidden-narrow="true"><div class="prc-PageLayout-Content-xWL-A" data-width="full" style="--spacing:var(--spacing-none)"><div data-selector="repos-split-pane-content" tabindex="0" class="Box-sc-62in7e-0 cybVuK"><div class="Box-sc-62in7e-0 gSjuRy"><div class="container CodeViewHeader-module__Box__JkPOb"><div class="tmp-px-3 tmp-pt-3 pb-0" id="StickyHeader" style="position: sticky;"><div class="CodeViewHeader-module__Box_1__SbNDV"><div class="CodeViewHeader-module__Box_2__TB46f"><div class="CodeViewHeader-module__Box_6__qKUtX"><div class="Breadcrumb-module__container__Vxvev Breadcrumb-module__lg__Rjz0A"><nav data-testid="breadcrumbs" aria-labelledby="repos-header-breadcrumb--wide-heading" id="repos-header-breadcrumb--wide" class="Breadcrumb-module__nav__rQFDj"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading" id="repos-header-breadcrumb--wide-heading">Breadcrumbs</h2><ol class="Breadcrumb-module__list__ZH6zr"><li class="Breadcrumb-module__listItem__Ib0x_"><a class="Breadcrumb-module__repoLink__O2Nbs prc-Link-Link-9ZwDx" data-testid="breadcrumbs-repo-link" href="https://github.com/khavadim1-cyber/pp2_v_kha/tree/main" data-discover="true">pp2_v_kha</a></li><li class="Breadcrumb-module__listItem__Ib0x_"><span class="Breadcrumb-module__separator__eNwsI Breadcrumb-module__lg__Rjz0A" aria-hidden="true">/</span><a class="Breadcrumb-module__directoryLink__kQy_t prc-Link-Link-9ZwDx" href="https://github.com/khavadim1-cyber/pp2_v_kha/tree/main/practise3" data-discover="true">practise3</a></li><li class="Breadcrumb-module__listItem__Ib0x_"><span class="Breadcrumb-module__separator__eNwsI Breadcrumb-module__lg__Rjz0A" aria-hidden="true">/</span><a class="Breadcrumb-module__directoryLink__kQy_t prc-Link-Link-9ZwDx" href="https://github.com/khavadim1-cyber/pp2_v_kha/tree/main/practise3/classes" data-discover="true">classes</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Breadcrumb-module__filename__equZR"><span class="Breadcrumb-module__separator__eNwsI Breadcrumb-module__lg__Rjz0A" aria-hidden="true">/</span><h1 class="Breadcrumb-module__filenameHeading__MNMtw Breadcrumb-module__lg__Rjz0A prc-Heading-Heading-MtWFE" tabindex="-1" id="file-name-id-wide">class_defenition.py</h1></div><button data-component="IconButton" type="button" class="prc-Button-ButtonBase-9n-Xk ml-2 prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-labelledby="_R_3b9lab_"><svg aria-hidden="true" focusable="false" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button><span class="CopyToClipboardButton-module__tooltip__BhMvU prc-TooltipV2-Tooltip-tLeuB" data-direction="nw" aria-label="Copy path" aria-hidden="true" id="_R_3b9lab_" popover="auto">Copy path</span></div></div><div class="react-code-view-header-element--wide"><div class="CodeViewHeader-module__Box_7___0R6c"><div class="d-flex gap-2"> <button hidden="" data-testid="" data-hotkey="l,Shift+L" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="l,Shift+L"></button><button hidden="" data-testid="" data-hotkey="Mod+Alt+g" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Mod+Alt+g"></button><button type="button" data-hotkey="b,Shift+B,Control+/ Control+b" class="prc-Button-ButtonBase-9n-Xk Button__StyledButtonComponent-sc-vqy3e4-0 hfSsoj NavigationMenu-module__Button__LpKgm" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3">Blame</span></span></button><button hidden="" data-testid="" data-hotkey="b,Shift+B,Control+/ Control+b" data-hotkey-scope="read-only-cursor-text-area"></button><button data-component="IconButton" type="button" data-testid="more-file-actions-button-nav-menu-wide" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk js-blob-dropdown-click NavigationMenu-module__IconButton__HpX3G prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-labelledby="_r_5s_" id="_r_5q_"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="nw" aria-hidden="true" id="_r_5s_" popover="auto">More file actions</span> </div></div></div><div class="react-code-view-header-element--narrow"><div class="CodeViewHeader-module__Box_7___0R6c"><div class="d-flex gap-2"> <button hidden="" data-testid="" data-hotkey="l,Shift+L" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="l,Shift+L"></button><button hidden="" data-testid="" data-hotkey="Mod+Alt+g" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Mod+Alt+g"></button><button type="button" data-hotkey="b,Shift+B,Control+/ Control+b" class="prc-Button-ButtonBase-9n-Xk Button__StyledButtonComponent-sc-vqy3e4-0 hfSsoj NavigationMenu-module__Button__LpKgm" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3">Blame</span></span></button><button hidden="" data-testid="" data-hotkey="b,Shift+B,Control+/ Control+b" data-hotkey-scope="read-only-cursor-text-area"></button><button data-component="IconButton" type="button" data-testid="more-file-actions-button-nav-menu-narrow" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk js-blob-dropdown-click NavigationMenu-module__IconButton__HpX3G prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-labelledby="_r_61_" id="_r_5v_"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="nw" aria-hidden="true" id="_r_61_" popover="auto">More file actions</span> </div></div></div></div></div></div></div></div><div class="Box-sc-62in7e-0 jyTWxL react-code-view-bottom-padding"> <div class="BlobTopBanners-module__Box__v_nvx"></div>   </div><div class="Box-sc-62in7e-0 jyTWxL">   <button hidden="" data-testid="" data-hotkey="r,Shift+R" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="r,Shift+R"></button><div class="d-flex flex-column border rounded-2 tmp-mb-3 pl-1"><div class="LatestCommit-module__Box__B25ZT"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading">Latest commit</h2><div data-testid="latest-commit" class="LatestCommit-module__Box_1__YkEgg"><div class="CommitAttribution-module__CommitAttributionContainer__I_rfs"><div data-testid="author-avatar" class="Box-sc-62in7e-0 AuthorAvatar-module__AuthorAvatarContainer__n0MVc"><img data-component="Avatar" class="Box-sc-62in7e-0 kglDHV AuthorAvatar-module__authorAvatarImage__a3R8x prc-Avatar-Avatar-0xaUi" alt="author" width="20" height="20" data-testid="github-avatar" aria-label="author" src="./def_files/gravatar-user-420.png" style="--avatarSize-regular: 20px;"><div class="AuthorDisplayName-module__truncate__d1MRu prc-Truncate-Truncate-2G1eo" data-inline="true" title="Vadim Kha" style="--truncate-max-width: 125px;"><span class="Text__StyledText-sc-1klmep6-0 iqjEaj AuthorDisplayName-module__Text__OP5Q9 prc-Text-Text-9mHv3">Vadim Kha</span></div></div><span class=""></span></div><div class="d-none d-sm-flex LatestCommit-module__Box_2__pSPKJ"><div class="Truncate flex-items-center f5"><span class="Text__StyledText-sc-1klmep6-0 Truncate-text prc-Text-Text-9mHv3" data-testid="latest-commit-html"><a href="https://github.com/khavadim1-cyber/pp2_v_kha/commit/6d8882875f98877c5aab86a383be71619a9634cd" class="Link--secondary" data-pjax="true" data-hovercard-url="/khavadim1-cyber/pp2_v_kha/commit/6d8882875f98877c5aab86a383be71619a9634cd/hovercard" aria-keyshortcuts="Alt+ArrowUp">add inheritance</a></span></div></div><span class="d-flex d-sm-none fgColor-muted f6"><relative-time tense="past" datetime="2026-02-07T06:03:48.000Z" title="Feb 7, 2026, 11:03 AM GMT+5"><template shadowrootmode="open">last week</template>Feb 7, 2026</relative-time></span></div><div class="d-flex flex-shrink-0 gap-2"><div data-testid="latest-commit-details" class="d-none d-sm-flex flex-items-center"><span class="d-flex flex-nowrap fgColor-muted f6"><a class="Link--secondary prc-Link-Link-9ZwDx" aria-label="Commit 6d88828" data-hovercard-url="/khavadim1-cyber/pp2_v_kha/commit/6d8882875f98877c5aab86a383be71619a9634cd/hovercard" data-hovercard-type="commit" octo-click="hovercard-link-click" octo-dimensions="link_type:self" aria-keyshortcuts="Alt+ArrowUp" href="https://github.com/khavadim1-cyber/pp2_v_kha/commit/6d8882875f98877c5aab86a383be71619a9634cd" data-discover="true">6d88828</a>&nbsp;·&nbsp;<relative-time tense="past" datetime="2026-02-07T06:03:48.000Z" title="Feb 7, 2026, 11:03 AM GMT+5"><template shadowrootmode="open">last week</template>Feb 7, 2026</relative-time></span></div><div class="d-flex gap-2"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading">History</h2><a href="https://github.com/khavadim1-cyber/pp2_v_kha/commits/main/practise3/classes/class_defenition.py" class="prc-Button-ButtonBase-9n-Xk d-none d-lg-flex LinkButton-module__linkButton__nFnov flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3"><span class="fgColor-default">History</span></span></span></a><div class="d-sm-none"><button data-component="IconButton" type="button" aria-pressed="false" aria-expanded="false" data-testid="latest-commit-details-toggle" class="prc-Button-ButtonBase-9n-Xk LatestCommit-module__IconButton__mkJr_ prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-labelledby="_r_9v_"><svg aria-hidden="true" focusable="false" class="octicon octicon-ellipsis" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M0 5.75C0 4.784.784 4 1.75 4h12.5c.966 0 1.75.784 1.75 1.75v4.5A1.75 1.75 0 0 1 14.25 12H1.75A1.75 1.75 0 0 1 0 10.25ZM12 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2ZM7 8a1 1 0 1 0 2 0 1 1 0 0 0-2 0ZM4 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id="_r_9v_" popover="auto">Open commit details</span></div><div class="d-flex d-lg-none"><a aria-label="View commit history for this file." href="https://github.com/khavadim1-cyber/pp2_v_kha/commits/main/practise3/classes/class_defenition.py" class="prc-Button-ButtonBase-9n-Xk LinkButton-module__linkButton__nFnov flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible" aria-describedby="_r_64_"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span></span></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" role="tooltip" aria-hidden="true" id="_r_64_" popover="auto">History</span></div></div></div></div></div><div class="Box-sc-62in7e-0 hGzGyY"><div class="Box-sc-62in7e-0 cJXRZE container"><div class="Box-sc-62in7e-0 fpyUWF react-code-size-details-banner"><div class="react-code-size-details-banner CodeSizeDetails-module__Box__VcD6l"><div class="text-mono CodeSizeDetails-module__Box_1__GVxQL"><div data-testid="blob-size" class="CodeSizeDetails-module__Truncate_1__lE93V prc-Truncate-Truncate-2G1eo" data-inline="true" title="257 Bytes" style="--truncate-max-width: 100%;"><span>16 lines (14 loc) · 257 Bytes</span></div></div></div></div><div class="Box-sc-62in7e-0 iafbuG react-blob-view-header-sticky" id="repos-sticky-header"><div class="BlobViewHeader-module__Box__yhm9u"><div class="react-blob-sticky-header"><div class="Box-sc-62in7e-0 iNRqcN"><div class="FileNameStickyHeader-module__Box_5__dmNXA"><div class="Breadcrumb-module__container__Vxvev Breadcrumb-module__md__Wb1Gs"><nav data-testid="breadcrumbs" aria-labelledby="sticky-breadcrumb-heading" id="sticky-breadcrumb" class="Breadcrumb-module__nav__rQFDj"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading" id="sticky-breadcrumb-heading">Breadcrumbs</h2><ol class="Breadcrumb-module__list__ZH6zr"><li class="Breadcrumb-module__listItem__Ib0x_"><a class="Breadcrumb-module__repoLink__O2Nbs prc-Link-Link-9ZwDx" data-testid="breadcrumbs-repo-link" href="https://github.com/khavadim1-cyber/pp2_v_kha/tree/main" data-discover="true">pp2_v_kha</a></li><li class="Breadcrumb-module__listItem__Ib0x_"><span class="Breadcrumb-module__separator__eNwsI Breadcrumb-module__md__Wb1Gs" aria-hidden="true">/</span><a class="Breadcrumb-module__directoryLink__kQy_t prc-Link-Link-9ZwDx" href="https://github.com/khavadim1-cyber/pp2_v_kha/tree/main/practise3" data-discover="true">practise3</a></li><li class="Breadcrumb-module__listItem__Ib0x_"><span class="Breadcrumb-module__separator__eNwsI Breadcrumb-module__md__Wb1Gs" aria-hidden="true">/</span><a class="Breadcrumb-module__directoryLink__kQy_t prc-Link-Link-9ZwDx" href="https://github.com/khavadim1-cyber/pp2_v_kha/tree/main/practise3/classes" data-discover="true">classes</a></li></ol></nav><div data-testid="breadcrumbs-filename" class="Breadcrumb-module__filename__equZR"><span class="Breadcrumb-module__separator__eNwsI Breadcrumb-module__md__Wb1Gs" aria-hidden="true">/</span><h1 class="Breadcrumb-module__filenameHeading__MNMtw Breadcrumb-module__md__Wb1Gs prc-Heading-Heading-MtWFE" tabindex="-1" id="sticky-file-name-id">class_defenition.py</h1></div></div><button type="button" class="prc-Button-ButtonBase-9n-Xk Button__StyledButtonComponent-sc-vqy3e4-0 FileNameStickyHeader-module__Button__LSEU_ FileNameStickyHeader-module__GoToTopButton__nxAFn" data-loading="false" data-size="small" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-arrow-up" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M3.47 7.78a.75.75 0 0 1 0-1.06l4.25-4.25a.75.75 0 0 1 1.06 0l4.25 4.25a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018L9 4.81v7.44a.75.75 0 0 1-1.5 0V4.81L4.53 7.78a.75.75 0 0 1-1.06 0Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3">Top</span></span></button></div></div></div><div class="BlobViewHeader-module__Box_1__VEmuQ"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone__rwWIk prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading">File metadata and controls</h2><div class="BlobViewHeader-module__Box_2__icUs2"><ul aria-label="File view" class="prc-SegmentedControl-SegmentedControl-lqIXp BlobTabButtons-module__SegmentedControl__jen2u" data-variant="default" data-size="small"><li class="prc-SegmentedControl-Item-tSCQh" data-selected=""><button aria-current="true" class="prc-SegmentedControl-Button-E48xz" type="button" data-hotkey="Control+/ Control+c" style="--separator-color: transparent;"><span class="prc-SegmentedControl-Content-1COlk segmentedControl-content"><div class="prc-SegmentedControl-Text-7S2y2 segmentedControl-text" data-text="Code">Code</div></span></button></li><li class="prc-SegmentedControl-Item-tSCQh"><button aria-current="false" class="prc-SegmentedControl-Button-E48xz" type="button" data-hotkey="b,Shift+B,Control+/ Control+b" style="--separator-color: var(--borderColor-default);"><span class="prc-SegmentedControl-Content-1COlk segmentedControl-content"><div class="prc-SegmentedControl-Text-7S2y2 segmentedControl-text" data-text="Blame">Blame</div></span></button></li></ul><button hidden="" data-testid="" data-hotkey="Control+/ Control+c" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="" data-hotkey="b,Shift+B,Control+/ Control+b" data-hotkey-scope="read-only-cursor-text-area"></button><div class="react-code-size-details-in-header CodeSizeDetails-module__Box__VcD6l"><div class="text-mono CodeSizeDetails-module__Box_1__GVxQL"><div data-testid="blob-size" class="CodeSizeDetails-module__Truncate_1__lE93V prc-Truncate-Truncate-2G1eo" data-inline="true" title="257 Bytes" style="--truncate-max-width: 100%;"><span>16 lines (14 loc) · 257 Bytes</span></div></div></div></div><div class="BlobViewHeader-module__Box_3__ng6v2"><button hidden="" data-testid="" data-hotkey="Control+Shift+&gt;" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Control+Shift+&gt;"></button><button hidden="" data-testid="" data-hotkey="Control+Shift+&lt;" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-hotkey="Control+Shift+&lt;"></button><button data-component="IconButton" type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-labelledby="_r_6a_" id="_r_69_"><svg aria-hidden="true" focusable="false" class="octicon octicon-space" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M0 13.25V2.75C0 1.784.784 1 1.75 1H5c.551 0 1.07.26 1.4.7l.9 1.2a.25.25 0 0 0 .2.1h6.75c.966 0 1.75.784 1.75 1.75v3.638a.75.75 0 0 1-1.5 0V4.75a.25.25 0 0 0-.25-.25H7.5a1.75 1.75 0 0 1-1.4-.7l-.9-1.2a.25.25 0 0 0-.2-.1H1.75a.25.25 0 0 0-.25.25v10.5c0 .138.112.25.25.25h5.663l.076.004a.75.75 0 0 1 0 1.492L7.413 15H1.75A1.75 1.75 0 0 1 0 13.25Z"></path><path d="M12.265 9.16a.248.248 0 0 1 .467 0l.237.649a3.726 3.726 0 0 0 2.219 2.218l.649.238a.249.249 0 0 1 0 .467l-.649.237a3.728 3.728 0 0 0-2.219 2.219l-.237.649a.249.249 0 0 1-.467 0l-.238-.649a3.726 3.726 0 0 0-2.218-2.219l-.649-.237a.248.248 0 0 1 0-.467l.649-.238a3.725 3.725 0 0 0 2.218-2.218l.238-.649Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="n" aria-hidden="true" id="_r_6a_" popover="auto">Add to space</span><button data-component="IconButton" type="button" data-testid="copilot-ask-menu" class="prc-Button-ButtonBase-9n-Xk prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-labelledby="_r_6c_" id="blob-view-header-copilot-icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-copilot" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="n" aria-hidden="true" id="_r_6c_" popover="auto">Ask Copilot about this file</span><div class="react-blob-header-edit-and-raw-actions BlobViewHeader-module__Box_4__J4Y4W"><div class="prc-ButtonGroup-ButtonGroup-vFUrY"><div><a href="https://github.com/khavadim1-cyber/pp2_v_kha/raw/refs/heads/main/practise3/classes/class_defenition.py" data-testid="raw-button" data-hotkey="Control+/ Control+r" class="prc-Button-ButtonBase-9n-Xk LinkButton-module__linkButton__nFnov BlobViewHeader-module__LinkButton__X9kx2" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3">Raw</span></span></a></div><div><button data-component="IconButton" type="button" data-testid="copy-raw-button" data-hotkey="Control+Shift+C" class="prc-Button-ButtonBase-9n-Xk prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-labelledby="_r_6f_"><svg aria-hidden="true" focusable="false" class="octicon octicon-copy" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="n" aria-hidden="true" id="_r_6f_" popover="auto">Copy raw file</span></div><div><button data-component="IconButton" type="button" data-testid="download-raw-button" data-hotkey="Control+Shift+S" sx="[object Object]" class="prc-Button-ButtonBase-9n-Xk prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-labelledby="_r_6h_"><svg aria-hidden="true" focusable="false" class="octicon octicon-download" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M2.75 14A1.75 1.75 0 0 1 1 12.25v-2.5a.75.75 0 0 1 1.5 0v2.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 14Z"></path><path d="M7.25 7.689V2a.75.75 0 0 1 1.5 0v5.689l1.97-1.969a.749.749 0 1 1 1.06 1.06l-3.25 3.25a.749.749 0 0 1-1.06 0L4.22 6.78a.749.749 0 1 1 1.06-1.06l1.97 1.969Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="n" aria-hidden="true" id="_r_6h_" popover="auto">Download raw file</span></div></div><button hidden="" data-testid="raw-button-shortcut" data-hotkey="Control+/ Control+r" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="copy-raw-button-shortcut" data-hotkey="Control+Shift+C" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="download-raw-button-shortcut" data-hotkey="Control+Shift+S" data-hotkey-scope="read-only-cursor-text-area"></button><a class="js-github-dev-shortcut d-none prc-Link-Link-9ZwDx" data-hotkey="., Control+Shift+/" href="https://github.dev/"></a><button hidden="" data-testid="" data-hotkey="., Control+Shift+/" data-hotkey-scope="read-only-cursor-text-area"></button><a class="js-github-dev-new-tab-shortcut d-none prc-Link-Link-9ZwDx" data-hotkey="Shift+.,Shift+&gt;,&gt;" href="https://github.dev/" target="_blank"></a><button hidden="" data-testid="" data-hotkey="Shift+.,Shift+&gt;,&gt;" data-hotkey-scope="read-only-cursor-text-area"></button><div class="prc-ButtonGroup-ButtonGroup-vFUrY"><div><a data-component="IconButton" type="button" data-hotkey="e,Shift+E" data-testid="edit-button" class="prc-Button-ButtonBase-9n-Xk LinkButton-module__linkButton__nFnov prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-labelledby="_r_6j_" href="https://github.com/khavadim1-cyber/pp2_v_kha/edit/main/practise3/classes/class_defenition.py" data-discover="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-pencil" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg></a><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="nw" aria-hidden="true" id="_r_6j_" popover="auto">Fork this repository and edit the file</span></div><div><button data-component="IconButton" type="button" data-testid="more-edit-button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="default" aria-labelledby="_r_6n_" id="_r_6l_"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="nw" aria-hidden="true" id="_r_6n_" popover="auto">More edit options</span></div></div><button hidden="" data-testid="" data-hotkey="e,Shift+E" data-hotkey-scope="read-only-cursor-text-area"></button></div><button data-component="IconButton" type="button" aria-pressed="false" aria-expanded="false" aria-controls="symbols-pane" data-hotkey="Control+i" data-testid="symbols-button" class="prc-Button-ButtonBase-9n-Xk BlobViewHeader-module__IconButton_2__RyjZg prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-labelledby="_r_6p_" id="symbols-button"><svg aria-hidden="true" focusable="false" class="octicon octicon-code-square" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25Zm7.47 3.97a.75.75 0 0 1 1.06 0l2 2a.75.75 0 0 1 0 1.06l-2 2a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L10.69 8 9.22 6.53a.75.75 0 0 1 0-1.06ZM6.78 6.53 5.31 8l1.47 1.47a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215l-2-2a.75.75 0 0 1 0-1.06l2-2a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="nw" aria-hidden="true" id="_r_6p_" popover="auto">Open symbols panel</span><div class="react-blob-header-edit-and-raw-actions-combined"><button data-component="IconButton" type="button" title="More file actions" data-testid="more-file-actions-button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk js-blob-dropdown-click BlobViewHeader-module__IconButton__XrMQY prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-labelledby="_r_6t_" id="_r_6r_"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="nw" aria-hidden="true" id="_r_6t_" popover="auto">Edit and raw actions</span></div></div></div></div><div></div></div><div class="Box-sc-62in7e-0 dIDnLY"><section aria-labelledby="file-name-id-wide file-name-id-mobile" class="Box-sc-62in7e-0 hhuNfn"><div class="Box-sc-62in7e-0 hNuvaP"><div id="highlighted-line-menu-positioner" class="position-relative"><div id="copilot-button-positioner" class="Box-sc-62in7e-0 kBkfpQ"><div class="Box-sc-62in7e-0 lnfLer"><div class="Box-sc-62in7e-0 ufhDn"><div class="Box-sc-62in7e-0 fIwdzP"><div aria-hidden="true" data-testid="navigation-cursor" class="Box-sc-62in7e-0 code-navigation-cursor" style="top: 140px; left: 184px;"> </div><button hidden="" data-testid="NavigationCursorEnter" data-hotkey="Control+Enter" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorSetHighlightedLine" data-hotkey="Shift+J" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorSetHighlightAndExpandMenu" data-hotkey="Alt+Shift+C,Alt+Shift+Ç" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorPageDown" data-hotkey="PageDown" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="NavigationCursorPageUp" data-hotkey="PageUp" data-hotkey-scope="read-only-cursor-text-area"></button><button hidden="" data-testid="" data-hotkey="/" data-hotkey-scope="read-only-cursor-text-area"></button></div></div><textarea id="read-only-cursor-text-area" data-testid="read-only-cursor-text-area" aria-label="file content" aria-readonly="true" inputmode="none" tabindex="0" aria-multiline="true" aria-haspopup="false" data-gramm="false" data-gramm_editor="false" data-enable-grammarly="false" spellcheck="false" autocorrect="off" autocapitalize="off" autocomplete="off" data-ms-editor="false" class="react-blob-textarea react-blob-print-hide" style="resize: none; margin-top: -2px; padding-left: 92px; padding-right: 70px; width: 100%; background-color: unset; box-sizing: border-box; color: transparent; position: absolute; border: none; tab-size: 4; outline: none; overflow: auto hidden; height: 340px; font-size: 12px; line-height: 20px; overflow-wrap: normal; overscroll-behavior-x: none; white-space: pre; z-index: 1;">class MyClass:#class defenition
  x = 5
  y =6
p=MyClass()#p-object
print(p.y, p.x)

p1 = MyClass()#creating multiple objects
p2 = MyClass()
p3 = MyClass()
print(p1.x)
print(p2.x)
print(p3.x)

class Person:#class cant be empty
  pass
del p1#deleting object</textarea><button hidden="" data-testid="" data-hotkey="Alt+F1,Control+Alt+˙,Control+Alt+h" data-hotkey-scope="read-only-cursor-text-area"></button><div class="Box-sc-62in7e-0 cZXDgG"><div tabindex="0" class="Box-sc-62in7e-0 cUUYDl"><div class="Box-sc-62in7e-0 dqWPVO react-code-file-contents" role="presentation" aria-hidden="true" data-tab-size="4" data-paste-markdown-skip="true" data-hpc="true"><div class="react-line-numbers-no-virtualization" style="pointer-events: auto; position: relative; z-index: 2;"><div class="react-no-virtualization-wrapper-lines"><div data-line-number="1" class="react-line-number react-code-text" style="padding-right: 16px;">1</div><div data-line-number="2" class="react-line-number react-code-text" style="padding-right: 16px;">2</div><div data-line-number="3" class="react-line-number react-code-text" style="padding-right: 16px;">3</div><div data-line-number="4" class="react-line-number react-code-text" style="padding-right: 16px;">4</div><div data-line-number="5" class="react-line-number react-code-text" style="padding-right: 16px;">5</div><div data-line-number="6" class="react-line-number react-code-text" style="padding-right: 16px;">6</div><div data-line-number="7" class="react-line-number react-code-text" style="padding-right: 16px;">7</div><div data-line-number="8" class="react-line-number react-code-text" style="padding-right: 16px;">8</div><div data-line-number="9" class="react-line-number react-code-text" style="padding-right: 16px;">9</div><div data-line-number="10" class="react-line-number react-code-text" style="padding-right: 16px;">10</div><div data-line-number="11" class="react-line-number react-code-text" style="padding-right: 16px;">11</div><div data-line-number="12" class="react-line-number react-code-text" style="padding-right: 16px;">12</div><div data-line-number="13" class="react-line-number react-code-text" style="padding-right: 16px;">13</div><div data-line-number="14" class="react-line-number react-code-text" style="padding-right: 16px;">14</div><div data-line-number="15" class="react-line-number react-code-text" style="padding-right: 16px;">15</div><div data-line-number="16" class="react-line-number react-code-text" style="padding-right: 16px;">16</div></div></div><div class="react-code-lines"><div inert=""><div class="react-no-virtualization-wrapper"><div id="LC1" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">class</span> <span class="pl-v">MyClass</span>:<span class="pl-c">#class defenition</span></div>
<div id="LC2" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">  <span class="pl-s1">x</span> <span class="pl-c1">=</span> <span class="pl-c1">5</span></div>
<div id="LC3" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">  <span class="pl-s1">y</span> <span class="pl-c1">=</span><span class="pl-c1">6</span></div>
<div id="LC4" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">p</span><span class="pl-c1">=</span><span class="pl-en">MyClass</span>()<span class="pl-c">#p-object</span></div>
<div id="LC5" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-en">print</span>(<span class="pl-s1">p</span>.<span class="pl-c1">y</span>, <span class="pl-s1">p</span>.<span class="pl-c1">x</span>)</div>
<div id="LC6" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC7" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">p1</span> <span class="pl-c1">=</span> <span class="pl-en">MyClass</span>()<span class="pl-c">#creating multiple objects</span></div>
<div id="LC8" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">p2</span> <span class="pl-c1">=</span> <span class="pl-en">MyClass</span>()</div>
<div id="LC9" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-s1">p3</span> <span class="pl-c1">=</span> <span class="pl-en">MyClass</span>()</div>
<div id="LC10" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-en">print</span>(<span class="pl-s1">p1</span>.<span class="pl-c1">x</span>)</div>
<div id="LC11" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-en">print</span>(<span class="pl-s1">p2</span>.<span class="pl-c1">x</span>)</div>
<div id="LC12" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-en">print</span>(<span class="pl-s1">p3</span>.<span class="pl-c1">x</span>)</div>
<div id="LC13" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">
</div>
<div id="LC14" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">class</span> <span class="pl-v">Person</span>:<span class="pl-c">#class cant be empty</span></div>
<div id="LC15" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div ">  <span class="pl-k">pass</span></div>
<div id="LC16" class="react-code-text react-code-line-contents-no-virtualization react-file-line html-div "><span class="pl-k">del</span> <span class="pl-s1">p1</span><span class="pl-c">#deleting object</span></div></div></div></div><button hidden="" data-hotkey="Control+a"></button></div></div></div></div><div id="copilot-button-container"></div></div><div id="highlighted-line-menu-container"></div></div></div></section></div></div></div>   </div></div></div></div></div></div></div><div id="find-result-marks-container" class="Box-sc-62in7e-0 vdPNv"></div><button hidden="" data-testid="" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="Control+F6,Control+Shift+F6"></button><button hidden="" data-hotkey="Control+F6,Control+Shift+F6"></button></div> <!-- --> <!-- --> <script type="application/json" id="__PRIMER_DATA__R_0___">{"resolvedServerColorMode":"night"}</script></div>
</react-app>
</turbo-frame>


    </main>
  </div>

  </div>

          <footer class="footer pt-7 pb-6 f6 color-fg-muted color-border-subtle p-responsive" role="contentinfo" hidden="">
  <h2 class="sr-only">Footer</h2>

  


  <div class="d-flex flex-justify-center flex-items-center flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap">
    <div class="d-flex flex-items-center flex-shrink-0 mx-2">
      <a aria-label="GitHub Homepage" class="footer-octicon mr-2" href="https://github.com/">
        <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M12 1C5.923 1 1 5.923 1 12c0 4.867 3.149 8.979 7.521 10.436.55.096.756-.233.756-.522 0-.262-.013-1.128-.013-2.049-2.764.509-3.479-.674-3.699-1.292-.124-.317-.66-1.293-1.127-1.554-.385-.207-.936-.715-.014-.729.866-.014 1.485.797 1.691 1.128.99 1.663 2.571 1.196 3.204.907.096-.715.385-1.196.701-1.471-2.448-.275-5.005-1.224-5.005-5.432 0-1.196.426-2.186 1.128-2.956-.111-.275-.496-1.402.11-2.915 0 0 .921-.288 3.024 1.128a10.193 10.193 0 0 1 2.75-.371c.936 0 1.871.123 2.75.371 2.104-1.43 3.025-1.128 3.025-1.128.605 1.513.221 2.64.111 2.915.701.77 1.127 1.747 1.127 2.956 0 4.222-2.571 5.157-5.019 5.432.399.344.743 1.004.743 2.035 0 1.471-.014 2.654-.014 3.025 0 .289.206.632.756.522C19.851 20.979 23 16.854 23 12c0-6.077-4.922-11-11-11Z"></path>
</svg>
</a>
      <span>
        © 2026 GitHub,&nbsp;Inc.
      </span>
    </div>

    <nav aria-label="Footer">
      <h3 class="sr-only" id="sr-footer-heading">Footer navigation</h3>

      <ul class="list-style-none d-flex flex-justify-center flex-wrap mb-2 mb-lg-0" aria-labelledby="sr-footer-heading">

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link--secondary Link">Terms</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link--secondary Link">Privacy</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security" data-view-component="true" class="Link--secondary Link">Security</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}" href="https://www.githubstatus.com/" data-view-component="true" class="Link--secondary Link">Status</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to community&quot;,&quot;label&quot;:&quot;text:community&quot;}" href="https://github.community/" data-view-component="true" class="Link--secondary Link">Community</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to docs&quot;,&quot;label&quot;:&quot;text:docs&quot;}" href="https://docs.github.com/" data-view-component="true" class="Link--secondary Link">Docs</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}" href="https://support.github.com/?tags=dotcom-footer" data-view-component="true" class="Link--secondary Link">Contact</a>
          </li>

          <li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;cookies&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;cookies_link_subfooter_footer&quot;}">
       Manage cookies
    </button>
  </cookie-consent-link>
</li>

<li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent text-left" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;dont_share_info&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;dont_share_info_link_subfooter_footer&quot;}">
      Do not share my personal information
    </button>
  </cookie-consent-link>
</li>

      </ul>
    </nav>
  </div>
</footer>



    <ghcc-consent id="ghcc" class="position-fixed bottom-0 left-0" style="z-index: 999999" data-locale="en" data-initial-cookie-consent-allowed="" data-cookie-consent-required="false" data-catalyst=""></ghcc-consent>




  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden="">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

    <template id="site-details-dialog"></template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;"></div>
</div>

    <template id="snippet-clipboard-copy-button"></template>
<template id="snippet-clipboard-copy-button-unpositioned"></template>


    <style>
      .user-mention[href$="/serikkalijanaris-cyber"] {
        color: var(--color-user-mention-fg);
        background-color: var(--bgColor-attention-muted, var(--color-attention-subtle));
        border-radius: 2px;
        margin-left: -2px;
        margin-right: -2px;
      }
      .user-mention[href$="/serikkalijanaris-cyber"]:before,
      .user-mention[href$="/serikkalijanaris-cyber"]:after {
        content: '';
        display: inline-block;
        width: 2px;
      }
    </style>


    </div>
    <div id="js-global-screen-reader-notice" class="sr-only mt-n1" aria-live="polite" aria-atomic="true"></div>
    <div id="js-global-screen-reader-notice-assertive" class="sr-only mt-n1" aria-live="assertive" aria-atomic="true"></div>
  


<div class="sr-only mt-n1" id="screenReaderAnnouncementDiv" role="alert" data-testid="screenReaderAnnouncement" aria-live="assertive"></div><live-region><template shadowrootmode="open">
<style>
:host {
  border: 0;
  clip: rect(0 0 0 0);
  clip-path: inset(50%);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  white-space: nowrap;
  width: 1px;
}
</style>
<div id="polite" aria-live="polite" aria-atomic="true">lambda content loaded</div>
<div id="assertive" aria-live="assertive" aria-atomic="true"></div>
</template></live-region></body></html>